# -*- encoding=utf8 -*-
__author__ = "joycastle"

import sys
sys.path.append('tools.')
from tools.airtest.core.api import *
from airtest.cli.parser import cli_setup
from tools.poco.drivers.unity3d import UnityPoco

if not cli_setup():
    auto_setup(__file__, logdir="D:/testtools/testtools/airtest/log", devices=["Android:///",], project_root="D:/testtools/testtools/airtest")


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath="D:/testtools/testtools/airtest/log")