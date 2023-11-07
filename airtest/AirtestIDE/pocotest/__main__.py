import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from runtest import BingoVTestCase

if __name__ in '__main__':
    BingoVTestCase().tearDown()
