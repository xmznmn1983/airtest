# -*- encoding=utf8 -*-
__author__ = "joycastle"

import time
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()


def click_button(button):
    poco(button).wait_for_appearance()
    if poco(button).exists():
        poco(button).click()
    else:
        try:
            raise Exception()
        except:
            raise

#click_button(element_path.login)
