import sys
sys.path.append("pocotest")
from pocotest.poco_driver import BingoVTestCase
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from airtest.report.report import simple_report


class Start(BingoVTestCase):

    def setUp(self):
        self.log = "E:\\test\\testtools\\airtest"
        self.airtest_path = "E:\\test\\testtools\\airtest\\log"
        self.app_package = "com.bingo.cruise.free.best.top.game"
        self.package_path = "D:/Downloads/BingoVoyage_dev_android_package_1613_pocotest_test_1.22.1.apk"
        import pocotest.element_path
        self.element_path = pocotest.element_path
        os.system("adb devices")

        if not cli_setup():
            auto_setup(__file__, logdir=self.log,
                       devices=["Android://127.0.0.1:5037/emulator-5554"], project_root=self.airtest_path)
            uninstall(self.app_package)
            time.sleep(1)
            install(self.package_path)
            time.sleep(1)
            start_app(self.app_package)
            time.sleep(10)

            # print("start...")
            import pocotest.action
            pocotest.action.click_button(self.element_path.login)
            time.sleep(1)
            stop_app(self.app_package)
            # generate html report

    def runTest(self):
        pass

    def tearDown(self):
        simple_report(__file__)


if __name__ in '__main__':
    Start()
