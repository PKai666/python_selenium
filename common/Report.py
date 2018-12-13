import unittest
import HTMLTestRunner
import time,os
from common.PrintLog import Log
CASEPATH = './TestCase'
REPORTPATH = './report'


class report(unittest.TestCase):
    def __init__(self):
        self.case_dir = os.path.abspath(CASEPATH)
        self.report_dir = os.path.abspath(REPORTPATH)

    def make_report(self):
        try:
            self.discover = unittest.defaultTestLoader.discover(self.case_dir,
                                                            pattern='*.py',
                                                            top_level_dir=None)
            self.ReportName = time.strftime('%Y-%m-%d %H-%M')
            self.report_path = os.path.join(self.report_dir, (self.ReportName+'.html'))

            fp = open(self.report_path, 'wb')
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                                        title='测试报告', description='用例执行情况')
            runner.run(self.discover)
            fp.close()
            Log().log_info('make report sucess')
        except:
            Log.log_info('make report fail')

    def get_reportName(self):
        return self.ReportName