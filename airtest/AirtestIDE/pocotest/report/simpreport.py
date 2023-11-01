import os.path
import time

from airtest.report.report import simple_report

def report():

    path = "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\airtest\\airtest\\AirtestIDE\\pocotest\\report\\"
    filepath = path + "filepath"
    logpath = path + "logpath"
    logfile = path + "logfile"
    output = path + "output"
    path_num = [filepath, logpath, logfile, output]
    for i in path_num:
        if os.path.exists(i):
            print("exist")
        else:
            os.mkdir(i, 777)
    time.sleep(20)
    simple_report(filepath=filepath, logpath=logpath, logfile=None, output=output)
