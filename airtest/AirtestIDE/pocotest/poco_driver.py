# -*- encoding=utf8 -*-
__author__ = "joycastle"

import sys
sys.path.append('.')
from unittest.case import TestCase
from poco.drivers.unity3d import UnityPoco
from airtest.cli.parser import cli_setup
from airtest.core.api import *

class BingoVTestCase(TestCase):
    test_log = "E:\\test\\testtools\\airtest"
    log_path = "E:\\test\\testtools\\airtest\\log"
    test_device = "Android://127.0.0.1:5037/R58M66VY68Y"

    @classmethod
    def setUpClass(cls, android_device=test_device, airtest_path=log_path, test_log=test_log):
        if not cli_setup():
            auto_setup(__file__, logdir=test_log,
                       devices=[android_device], project_root=airtest_path)
        super(BingoVTestCase, cls).setUpClass()
        cls.poco = UnityPoco()





