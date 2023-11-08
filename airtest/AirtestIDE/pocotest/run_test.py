import sys
from airtest.core.api import *
from report.simpreport import report
from connect_devices import BingoVSetup
import airtest.cli.parser as parser
import argparse

class BingoVTestCase:
    def __init__(self):
        self.app_package = "com.bingo.cruise.free.best.top.game"
        self.package_path = "D:/Downloads/BingoVoyage_dev_android_package_1613_pocotest_test_1.22.1.apk"
        par = parser.runner_parser(ap=argparse.ArgumentParser()).parse_args()
        self.test_case = par.log

    def installGame(self):
        BingoVSetup().setupGame()
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
        self.installGame()
        self.runGame()
        time.sleep(20)

        if self.test_case == "store":
            print("start checktickets...")
            import testcase.store as store
            store.openTicketsBar()
            store.checkTickets()

        self.closeGame()

    def tearDown(self):
        self.runTest()
        report()
