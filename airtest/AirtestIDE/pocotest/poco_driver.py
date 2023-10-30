# -*- encoding=utf8 -*-
__author__ = "joycastle"

import sys

sys.path.append('.')
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.report.report import simple_report
#import action
import element_path
app_package = "com.bingo.cruise.free.best.top.game"
package_path = "D:/Downloads/BingoVoyage_dev_android_package_1613_pocotest_test_1.22.1.apk"

# script content
print("start...")

airtest_path = "E:/test/testtools/airtest"

def main():
    if not cli_setup():
        auto_setup(__file__, logdir=airtest_path,
                   devices=["Android://127.0.0.1:5037/R58M66VY68Y"], project_root=airtest_path)
        uninstall(app_package)
        time.sleep(1)
        # install(package_path)
        time.sleep(1)
        start_app(app_package)
        time.sleep(10)
        # print("start...")
        #action.click_button(element_path.login)
        time.sleep(1)
        stop_app(app_package)
        # generate html report
    simple_report(__file__, logpath=airtest_path + "/log", output="111.html")


