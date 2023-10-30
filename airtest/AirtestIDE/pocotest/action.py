# -*- encoding=utf8 -*-
__author__ = "joycastle"

from poco.drivers.unity3d import UnityPoco
import element_path

poco = UnityPoco()


def click_button(button):
    if poco(button).exists():
        poco(button).wait_for_appearance()
        poco(button).click()
    else:
        try:
            raise Exception()
        except:
            raise

#click_button(element_path.login)
