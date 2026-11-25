"""EDT-02: read-only APK upgrade preflight; no device interaction."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def inspect(path, aapt, apksigner, run=subprocess.run):
    path = Path(path).resolve(strict=True)
    before = digest(path)
    def command(*args):
        return run(args, check=True, capture_output=True, text=True, timeout=60).stdout
    badging = command(aapt, 'dump', 'badging', str(path))
    match = re.search(r"^package: name='([^']+)' versionCode='([0-9]+)'", badging, re.M)
    require(match is not None, 'Cannot determine package/version')
    certs = command(apksigner, 'verify', '--print-certs', str(path))
    fingerprints = re.findall(r'^Signer #\d+ certificate SHA-256 digest:\s*([0-9a-fA-F]{64})\s*$', certs, re.M)
    require(len(fingerprints) == 1, 'Expected exactly one APK signer')
    require(before == digest(path), 'APK changed during inspection')
    return dict(package=match[1], version=int(match[2]), signer=fingerprints[0].lower(), sha256=before)


def compare(old, new, package, signer):
    require(re.fullmatch(r'[0-9a-fA-F]{64}', signer) is not None, 'Invalid expected certificate fingerprint')
    require(old['package'] == new['package'] == package, 'Package mismatch')
    require(old['signer'] == new['signer'] == signer.lower(), 'Certificate mismatch')
    require(0 < old['version'] < new['version'] <= 2100000000, 'Version must increase within supported range')
    require(old['sha256'] != new['sha256'], 'Identical APK bytes')
    return dict(status='static_preflight_pass', old=old, new=new,
                limitations='No installation, save, device, key custody or publication verification')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('old'); p.add_argument('new')
    for name in ('package', 'signer', 'aapt', 'apksigner'):
        p.add_argument('--' + name, required=True)
    a = p.parse_args()
    try:
        print(json.dumps(compare(inspect(a.old, a.aapt, a.apksigner),
                                 inspect(a.new, a.aapt, a.apksigner), a.package, a.signer), indent=2))
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        p.exit(1, 'Preflight failed: ' + str(exc) + '\n')


if __name__ == '__main__':
    main()
