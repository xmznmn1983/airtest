import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from rungame import BingoVTestCase as BV

if __name__ in '__main__':
    BV().tearDown()
