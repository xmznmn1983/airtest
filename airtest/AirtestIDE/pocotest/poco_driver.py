# -*- encoding=utf8 -*-
__author__ = "joycastle"

import sys
sys.path.append('.')
from unittest.case import TestCase
from poco.drivers.unity3d import UnityPoco


class BingoVTestCase(TestCase):
    poco = None

    @classmethod
    def setUpClass(cls):
        super(BingoVTestCase, cls).setUpClass()
        cls.poco = UnityPoco()





