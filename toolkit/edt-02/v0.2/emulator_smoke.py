"""Synthetic APK upgrade smoke test. Never target an existing application."""
import argparse
import re
import subprocess
from pathlib import Path
from preflight import inspect, verify_receipt

PACKAGE = 'com.example.edtfixture'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def exercise(adb, serial, old, new, run=subprocess.run):
    require(re.fullmatch(r'emulator-[0-9]+', serial), 'Explicit local emulator serial required')
    def cmd(*args, data=None):
        return run([str(adb), '-s', serial, *map(str,args)], input=data,
                   capture_output=True, check=True, timeout=90).stdout
    require(cmd('get-state').strip() == b'device', 'Emulator not ready')
    require(cmd('shell','getprop','ro.kernel.qemu').strip() == b'1', 'Not an Android emulator')
    require(cmd('shell','getprop','sys.boot_completed').strip() == b'1', 'Boot incomplete')
    installed = cmd('shell','pm','list','packages','-u',PACKAGE).decode().splitlines()
    require('package:'+PACKAGE not in [x.strip() for x in installed], 'Fixture already exists; use fresh emulator')
    require(b'Success' in cmd('install',old), 'Baseline installation failed')
    # Only a debuggable, purpose-built fixture can pass run-as.
    marker = b'EDT synthetic progress v1\n'
    cmd('shell','run-as',PACKAGE,'mkdir','-p','files')
    cmd('shell','-T','run-as '+PACKAGE+" sh -c 'cat > files/edt_marker'",data=marker)
    def check_marker():
        require(cmd('exec-out','run-as',PACKAGE,'cat','files/edt_marker') == marker,'Synthetic progress changed')
    def check_version(expected):
        output = cmd('shell','dumpsys','package',PACKAGE).decode()
        match = re.search(r'\bversionCode=(\d+)\b',output)
        require(match and int(match[1]) == expected,'Installed version mismatch')
    check_version(1)
    check_marker()
    require(b'Success' in cmd('install','-r',new),'Upgrade installation failed')
    check_version(2)
    check_marker()
    return {'status':'synthetic_fixture_upgrade_pass','scope':'One synthetic private file; no app launch or real save verification'}


def main():
    import json
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('old',type=Path); p.add_argument('new',type=Path)
    for name in ('adb','serial','aapt','apksigner','signer','old-hash','new-hash'):
        p.add_argument('--'+name,required=True)
    p.add_argument('--disposable-emulator',action='store_true',required=True)
    a=p.parse_args()
    old,new=a.old.resolve(strict=True),a.new.resolve(strict=True)
    verify_receipt(inspect(old,a.aapt,a.apksigner),inspect(new,a.aapt,a.apksigner),PACKAGE,a.signer,a.old_hash,a.new_hash,1,2)
    print(json.dumps(exercise(a.adb,a.serial,old,new),indent=2))

if __name__=='__main__':
    main()
