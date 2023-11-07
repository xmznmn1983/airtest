import sys
import time

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from report.simpreport import report


class BingoVSetup:
    def __init__(self):
        os.system("adb devices")
        import element_path
        self.element_path = element_path
        self.test_log = os.path.dirname(os.path.abspath(__file__)) + "\\report"
        self.log_path = os.path.dirname(os.path.abspath(__file__)) + "\\report\\log"
        self.test_device = "Android://127.0.0.1:5037/R5CT319J77J"

    def setupGame(self):
        if not cli_setup():
            auto_setup(__file__, logdir=self.log_path,
                       devices=[self.test_device], project_root=self.test_log, compress=90)


BingoVSetup().setupGame()




