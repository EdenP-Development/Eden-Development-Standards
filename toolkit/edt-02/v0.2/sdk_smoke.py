"""Real SDK smoke test; optional isolated emulator fixture, no production keys."""
import hashlib
import os
from pathlib import Path
import subprocess
import argparse
import json
import tempfile
from preflight import inspect, verify_receipt


def run(*args):
    return subprocess.run([str(x) for x in args], check=True, capture_output=True,
                          text=True, timeout=90).stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--emulator-serial')
    parser.add_argument('--disposable-emulator', action='store_true')
    args = parser.parse_args()
    if bool(args.emulator_serial) != args.disposable_emulator:
        parser.error('Emulator serial and disposable-emulator acknowledgement must be supplied together')
    sdk = Path(os.environ.get('ANDROID_SDK_ROOT') or os.environ['ANDROID_HOME'])
    candidates = [p for p in (sdk/'build-tools').iterdir()
                  if (p/'aapt').is_file() and (p/'apksigner').is_file()]
    def version(p):
        return tuple(int(x) for x in p.name.split('.') if x.isdigit())
    tools = max(candidates, key=version)
    android = max((p for p in (sdk/'platforms').glob('android-*') if (p/'android.jar').is_file()
                   and p.name.removeprefix('android-').isdigit()),
                  key=lambda p: int(p.name.removeprefix('android-')))/'android.jar'
    aapt, signer = tools/'aapt', tools/'apksigner'
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        key = root/'fixture.p12'
        # Ephemeral synthetic fixture key, never used by an actual app.
        run('keytool','-genkeypair','-alias','fixture','-keyalg','RSA','-keysize','2048',
            '-validity','2','-dname','CN=EDT synthetic fixture','-storetype','PKCS12',
            '-keystore',key,'-storepass','fixture-only','-keypass','fixture-only')
        def build(code, package='com.example.edtfixture'):
            manifest = root/'AndroidManifest.xml'
            manifest.write_text(f'<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="{package}" android:versionCode="{code}" android:versionName="{code}"><uses-sdk android:minSdkVersion="26" android:targetSdkVersion="35"/><application android:hasCode="false" android:debuggable="true" android:allowBackup="false"/></manifest>')
            unsigned = root/f'{package}-{code}-unsigned.apk'
            signed = root/f'{package}-{code}.apk'
            run(aapt,'package','-f','-M',manifest,'-I',android,'-F',unsigned)
            run(signer,'sign','--ks',key,'--ks-key-alias','fixture','--ks-pass','pass:fixture-only',
                '--key-pass','pass:fixture-only','--out',signed,unsigned)
            return signed
        old, new, wrong = build(1), build(2), build(3,'com.example.otherfixture')
        a, b, c = [inspect(p,aapt,signer) for p in (old,new,wrong)]
        # Fixture receipt is derived from the controlled test build, not a production trust anchor.
        fingerprint = hashlib.sha256(subprocess.run(
            ['keytool','-exportcert','-alias','fixture','-keystore',str(key),'-storepass','fixture-only'],
            check=True,capture_output=True,timeout=60).stdout).hexdigest()
        def check(x, y, old_path, new_path, ov, nv):
            return verify_receipt(x,y,'com.example.edtfixture',fingerprint,
                hashlib.sha256(old_path.read_bytes()).hexdigest(),
                hashlib.sha256(new_path.read_bytes()).hexdigest(),ov,nv)
        if check(a,b,old,new,1,2)['status'] != 'receipt_matched_static_preflight':
            raise RuntimeError('Compatible pair not accepted')
        for args in [(a,c,old,wrong,1,3),(b,a,new,old,2,1)]:
            try:
                check(*args)
            except ValueError:
                continue
            raise RuntimeError('Incompatible pair accepted')
        print('PASS: real SDK signed fixture pair; wrong package and downgrade rejected.')
        if args.emulator_serial:
            from emulator_smoke import exercise
            # Recheck exact bytes immediately before the isolated installation.
            check(inspect(old,aapt,signer),inspect(new,aapt,signer),old,new,1,2)
            print(json.dumps(exercise(sdk/'platform-tools'/'adb',args.emulator_serial,old,new),indent=2))
        else:
            print('No install or save test requested.')


if __name__ == '__main__':
    main()
