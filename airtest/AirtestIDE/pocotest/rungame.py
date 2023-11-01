import sys
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from report.simpreport import report


class BingoVTestCase:
    def __init__(self):
        os.system("adb devices")
        self.app_package = "com.bingo.cruise.free.best.top.game"
        self.package_path = "D:/Downloads/BingoVoyage_dev_android_package_1613_pocotest_test_1.22.1.apk"
        import element_path
        self.element_path = element_path
        self.test_log = os.path.dirname(os.path.abspath(__file__)) + "\\report"
        self.log_path = os.path.dirname(os.path.abspath(__file__)) + "\\report\\log"
        self.test_device = "Android://127.0.0.1:5037/R58M66VY68Y"
        if not cli_setup():
            auto_setup(__file__, logdir=self.log_path,
                       devices=[self.test_device], project_root=self.test_log)


    def runGame(self):
        uninstall(self.app_package)
        time.sleep(1)
        install(self.package_path)
        time.sleep(1)
        start_app(self.app_package)
        time.sleep(10)
        # print("start...")
        from action import click_button
        click_button(self.element_path.login)
        time.sleep(1)
        stop_app(self.app_package)
        # generate html report

    def runTest(self):
        self.runGame()

    def tearDown(self):
        self.runTest()
        report()
