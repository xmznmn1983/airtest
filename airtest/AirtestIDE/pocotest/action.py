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



def child_element_exist(el_name1, el_name2):
    if poco(el_name1).child(el_name2).exists():
        return True
    else:
        return False



