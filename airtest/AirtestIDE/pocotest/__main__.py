import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from rungame import BingoVTestCase as BV
setup = sys.argv[1]
closeGame = sys.argv[3]
testCase = sys.argv[2]


if __name__ in '__main__':
    BV().tearDown(setup, testCase, closeGame)
