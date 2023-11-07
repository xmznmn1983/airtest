import sys
from airtest.core.api import *
from report.simpreport import report


class BingoVTestCase:
    def __init__(self):
        self.app_package = "com.bingo.cruise.free.best.top.game"
        self.package_path = "D:/Downloads/BingoVoyage_dev_android_package_1613_pocotest_test_1.22.1.apk"

        self.set_install = sys.argv[1]
        self.run_game = sys.argv[2]
        self.set_close = sys.argv[3]

    def installGame(self):
        uninstall(self.app_package)
        print("uninstall...")
        time.sleep(1)
        install(self.package_path)
        print("install...")
        time.sleep(1)

    def runGame(self):
        start_app(self.app_package)
        print("start game...")
        time.sleep(1)

    def closeGame(self):
        stop_app(self.app_package)
        print("close game...")
        time.sleep(1)

    def runTest(self):
        if self.installGame() == "install":
            self.installGame()
        self.runGame()
        time.sleep(20)

        if self.run_game == "store":
            print("start checktickets...")
            import testcase.store as store
            store.openTicketsBar()
            store.checkTickets()

        if self.set_close == "close":
            print("start closeing...")
            self.closeGame()

    def tearDown(self):
        self.runTest()
        report()
