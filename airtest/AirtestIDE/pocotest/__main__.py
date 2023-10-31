import sys

sys.path.append("C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\_airtest\\airtest\\AirtestIDE\\pocotest")
from testcase.rungame import BingoVTestCase as BV

if __name__ in '__main__':
    BV().setUp()
    BV().test_runGame()
