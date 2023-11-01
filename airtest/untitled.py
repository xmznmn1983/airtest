# -*- encoding=utf8 -*-
__author__ = "joycastle"


from poco.drivers.unity3d import UnityPoco

poco = UnityPoco

poco("GuestLoginButton").click()


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)