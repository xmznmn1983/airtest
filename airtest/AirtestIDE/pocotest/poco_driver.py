# -*- encoding=utf8 -*-
__author__ = "joycastle"

import sys
sys.path.append('.')
from unittest.case import TestCase
from poco.drivers.unity3d import UnityPoco
from airtest.cli.parser import cli_setup
from airtest.core.api import *

class BingoVTestCase(TestCase):
    poco = None
    def setUp(self):
        self.log = "E:\\test\\testtools\\airtest"
        self.airtest_path = "E:\\test\\testtools\\airtest\\log"
        self.app_package = "com.bingo.cruise.free.best.top.game"
        self.package_path = "D:/Downloads/BingoVoyage_dev_android_package_1613_pocotest_test_1.22.1.apk"
        import pocotest.element_path
        self.element_path = pocotest.element_path
        self.android_device = "Android://127.0.0.1:5037/R58M66VY68Y"
        if not cli_setup():
            auto_setup(__file__, logdir=self.log,
                       devices=[self.android_device], project_root=self.airtest_path)

    @classmethod
    def setUpClass(cls):
        super(BingoVTestCase, cls).setUpClass()
        cls.poco = UnityPoco()





