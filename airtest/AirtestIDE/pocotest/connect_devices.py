from airtest.core.api import *
import argparse
import airtest.cli.parser as parser


class BingoVSetup:
    def __init__(self):
        os.system("adb devices")
        # self.a1 = sys.argv[5]
        import element_path
        self.element_path = element_path
        self.test_log = os.path.dirname(os.path.abspath(__file__)) + "\\report"
        self.log_path = os.path.dirname(os.path.abspath(__file__)) + "\\report\\log"
        self.test_device = "Android://127.0.0.1:5037/R5CT319J77J"

    def setupGame(self):
        auto_setup(basedir=__file__, logdir=self.log_path,
                   devices=[self.test_device], project_root=self.test_log, compress=90)
        # print(parser.runner_parser(ap=argparse.ArgumentParser()).parse_args())


# BingoVSetup().setupGame()