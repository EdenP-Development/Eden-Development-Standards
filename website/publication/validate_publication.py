"""Offline, fail-closed publication receipt check. No publishing or network access."""
import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

CHECKS = ("exact_build", "data_inventory", "audience_and_store_review",
          "contact_test", "private_intake_test", "rights_and_privacy_review",
          "owner_content_approval", "host_approval")
PLACEHOLDER = re.compile(r"\b(?:todo|tbd|placeholder|prepublication draft|publication hold|not approved|not effective)\b", re.I)

def validate(record, root):
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
    for key in ("channel", "version", "publisher"):
        value(key)
    for key, length in (("source_revision", 40), ("apk_sha256", 64)):
        if not re.fullmatch(r"[0-9a-f]{%d}" % length, value(key)):
            errors.append(key + ": invalid fingerprint")
    for key in ("contact", "private_reporting_contact"):
        v = value(key)
        if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", v) or v.lower().split("@")[-1] in ("example.com", "example.org", "example.net") or v.lower().endswith((".invalid", ".test", ".localhost")):
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
            if u.scheme != "https" or not u.hostname or u.username or u.password or u.query or u.fragment or u.hostname in ("example.com", "example.org", "example.net", "localhost") or u.hostname.endswith((".invalid", ".test", ".localhost")):
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
        except (OSError, ValueError):
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
