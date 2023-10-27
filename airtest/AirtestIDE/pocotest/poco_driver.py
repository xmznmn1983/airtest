# -*- encoding=utf8 -*-
__author__ = "joycastle"

import sys
import time

import poco

sys.path.append('.')
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.report.report import simple_report
import action
from poco.drivers.unity3d import UnityPoco
import element_path

app_package = "com.bingo.cruise.free.best.top.game"
package_path = "D:/Downloads/BingoVoyage_dev_android_package_1613_pocotest_test_1.22.1.apk"


# script content


def main():
    #stop_app(app_package)
    if not cli_setup():
        auto_setup(__file__, logdir="D:/testtools/testtools/airtest/log",
                   devices=["Android://127.0.0.1:5037/emulator-5554", ], project_root="D:/testtools/testtools/airtest")
        #uninstall(app_package)
        time.sleep(1)
        #install(package_path)
        time.sleep(1)
        start_app(app_package)
        time.sleep(10)
        # print("start...")
        action.click_button(element_path.login)
        time.sleep(1)
        stop_app(app_package)
        # generate html report
        simple_report(__file__, logpath="D:/testtools/testtools/airtest/log", output="111.html")
#poco_driver()