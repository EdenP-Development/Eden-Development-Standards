"""Offline, fail-closed publication receipt check. No publishing or network access."""
import argparse
import hashlib
import ipaddress
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

CHECKS = ("exact_build", "data_inventory", "audience_and_store_review",
          "contact_test", "private_intake_test", "rights_and_privacy_review",
          "owner_content_approval", "host_approval")
PLACEHOLDER = re.compile(r"\b(?:todo|tbd|placeholder|prepublication draft|publication hold|not approved|not effective)\b", re.I)

PRODUCTS = frozenset(("sudoku", "word-search", "grid-hunt", "crossroads", "sector-rebound", "eden-comms"))
def valid_host(host, *, fixture=False):
    if not host or host.endswith(".") or not host.isascii():
        return False
    host = host.lower()
    try:
        ipaddress.ip_address(host)
        return False
    except ValueError:
        pass
    labels = host.split(".")
    if len(host) > 253 or len(labels) < 2 or not all(re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?", x) for x in labels):
        return False
    if fixture:
        return host == "fixture.example"
    return not (labels[-1] in ("example", "invalid", "test", "localhost", "local", "internal", "onion") or not labels[-1].isalpha() or any(host == x or host.endswith("." + x) for x in ("example.com", "example.org", "example.net")))

def validate(record, root, *, fixture=False):
    errors = []
    if not isinstance(record, dict):
        return ["receipt must be an object"]
    def value(key):
        v = record.get(key)
        if not isinstance(v, str) or not v.strip() or PLACEHOLDER.search(v):
            errors.append(key + ": missing or placeholder")
            return ""
        return v
    if type(record.get("schema")) is not int or record["schema"] != 1:
        errors.append("unsupported schema")
    product = value("product")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", product):
        errors.append("invalid product slug")
    if fixture:
        if product != "fixture" or record.get("channel") != "synthetic":
            errors.append("fixture mode requires synthetic fixture identity")
    elif product not in PRODUCTS or record.get("channel") == "synthetic":
        errors.append("unrecognized production product or synthetic channel")
    for key in ("channel", "version", "publisher"):
        value(key)
    for key, length in (("source_revision", 40), ("apk_sha256", 64)):
        if not re.fullmatch(r"[0-9a-f]{%d}" % length, value(key)):
            errors.append(key + ": invalid fingerprint")
    for key in ("contact", "private_reporting_contact"):
        v = value(key)
        if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", v) or not valid_host(v.rsplit("@", 1)[-1], fixture=fixture):
            errors.append(key + ": invalid or reserved email")
    try:
        d = value("effective_date")
        if date.fromisoformat(d).isoformat() != d:
            raise ValueError()
    except ValueError:
        errors.append("effective_date: expected YYYY-MM-DD")
    urls = []
    for kind in ("privacy", "support"):
        url = value(kind + "_url")
        try:
            u = urlsplit(url)
            if u.scheme != "https" or not valid_host(u.hostname, fixture=fixture) or u.username is not None or u.password is not None or u.query or u.fragment or u.port not in (None, 443) or not u.path or any(c.isspace() or ord(c) < 32 for c in url):
                raise ValueError()
            urls.append(url)
        except ValueError:
            errors.append(kind + "_url: expected stable HTTPS URL")
        name = value(kind + "_file")
        digest = value(kind + "_sha256")
        expected = f"website/approved/{product}/{kind}.md"
        if name != expected:
            errors.append(kind + "_file: outside approved content allowlist")
            continue
        try:
            p = root / name
            if p.resolve() != root.resolve() / name or not p.is_file():
                raise ValueError()
            data = p.read_bytes()
            if hashlib.sha256(data).hexdigest() != digest:
                errors.append(kind + ": content hash mismatch")
            text = data.decode("utf-8")
            if not text.strip() or PLACEHOLDER.search(text):
                errors.append(kind + ": empty or draft content")
            # Require exact labeled metadata lines, not incidental substrings.
            required = {"Publisher": record.get("publisher"),
                        "Contact": record.get("contact"),
                        "Effective date": record.get("effective_date"),
                        "Canonical URL": record.get(kind + "_url")}
            if kind == "support":
                required["Private reporting contact"] = record.get("private_reporting_contact")
            for label, expected_value in required.items():
                matches = [line for line in text.splitlines() if line.startswith(label + ":")]
                if not isinstance(expected_value, str) or matches != [label + ": " + expected_value]:
                    errors.append(kind + ": inconsistent " + label)
        except (OSError, ValueError, RuntimeError):
            errors.append(kind + ": unreadable or unsafe content path")
    if len(urls) == 2 and urls[0] == urls[1]:
        errors.append("privacy and support URLs must be distinct")
    checks = record.get("checks")
    for key in CHECKS:
        if not isinstance(checks, dict) or checks.get(key) is not True:
            errors.append("unconfirmed check: " + key)
    if record.get("publication_authorized") is not True:
        errors.append("publication not authorized")
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", type=Path)
    args = parser.parse_args()
    try:
        record = json.loads(args.receipt.read_text(encoding="utf-8"))
        errors = validate(record, Path(__file__).resolve().parents[2])
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    print(json.dumps({"passed": not errors, "errors": errors}, indent=2))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
