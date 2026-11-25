import unittest
from unittest.mock import Mock
from types import SimpleNamespace
from emulator_smoke import exercise, PACKAGE

class SafetyTests(unittest.TestCase):
    def fake(self, existing=False, qemu=b'1', marker=b'EDT synthetic progress v1\n'):
        calls=[]
        def run(args, **kwargs):
            calls.append(args)
            command=args[3:]
            if command==['get-state']: out=b'device\n'
            elif command[-1]=='ro.kernel.qemu': out=qemu
            elif command[-1]=='sys.boot_completed': out=b'1'
            elif command[:4]==['shell','pm','list','packages']: out=('package:'+PACKAGE).encode() if existing else b''
            elif command[0]=='install': out=b'Success\n'
            elif command[:3]==['shell','dumpsys','package']: out=b'versionCode=2' if any(x[3:5]==['install','-r'] for x in calls) else b'versionCode=1'
            elif command[0]=='exec-out': out=marker
            else: out=b''
            return SimpleNamespace(stdout=out)
        return run,calls
    def test_physical_serial_rejected(self):
        run=Mock()
        with self.assertRaises(ValueError): exercise('adb','phone123','old','new',run)
        run.assert_not_called()
    def test_not_emulator(self):
        run,calls=self.fake(qemu=b'0')
        with self.assertRaises(ValueError): exercise('adb','emulator-5554','old','new',run)
        self.assertFalse(any(x[3]=='install' for x in calls))
    def test_existing_fixture(self):
        run,calls=self.fake(existing=True)
        with self.assertRaises(ValueError): exercise('adb','emulator-5554','old','new',run)
        self.assertFalse(any(x[3]=='install' for x in calls))
    def test_upgrade(self):
        run,calls=self.fake()
        self.assertEqual(exercise('adb','emulator-5554','old','new',run)['status'],'synthetic_fixture_upgrade_pass')
        self.assertEqual([x[3:] for x in calls if x[3]=='install'],[['install','old'],['install','-r','new']])
        self.assertTrue(all(x[1:3]==['-s','emulator-5554'] for x in calls))
    def test_marker_mismatch(self):
        run,calls=self.fake(marker=b'wrong')
        with self.assertRaises(ValueError): exercise('adb','emulator-5554','old','new',run)
        self.assertFalse(any(x[3:5]==['install','-r'] for x in calls))
