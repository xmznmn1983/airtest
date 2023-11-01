import os.path
import time
from airtest.core import settings
from airtest.report.report import simple_report
from airtest.report.report import LogToHtml


def report():
    py_path = os.path.dirname(os.path.abspath(__file__))
    log_time = int(time.time())
    log_path = py_path + "\log"
    export_report = py_path + "\export"
    logfile = py_path + "\log\log.txt"
    path_num = [export_report]
    for i in path_num:
        if os.path.exists(i):
            print("exist")
        else:
            os.mkdir(i, 777)
    # time.sleep(20)
    #simple_report(__file__, logpath=True, output=r"D:\testtools\testtools\airtest\AirtestIDE\pocotest\report\logfile\log.html")
    #simple_report(__file__,logpath=True,output=r"D:\test\report02\log.html")
    h1 = LogToHtml(script_root=__file__, log_root=(r"%s" %log_path), export_dir=(r"%s" %export_report),
                   logfile=(r'%s' %logfile), lang='en', plugins=None)
    h1.report()


