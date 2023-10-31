# -*- encoding=utf8 -*-
__author__ = "joycastle"

import sys
from unittest.case import TestCase
sys.path.append('.')
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from pocounit.addons.poco.action_tracking import ActionTracker
from airtest.report.report import simple_report
from poco.drivers.unity3d import UnityPoco


class BingoVTestCase(TestCase):
    poco = None

    @classmethod
    def setUpClass(cls):
        super(BingoVTestCase, cls).setUpClass()
        cls.poco = UnityPoco()





