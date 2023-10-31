import os, sys
basedir2 = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(basedir2)
print(sys.path)
#print(sys.path.append(basedir2))