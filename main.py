
from common.ReadExcel import readExcel
from common.ReadConfig import readConf
from datetime import datetime
from common.PrintLog import Log
from common.SendEmail import sendEmail
from common.Report import report
from TestCase.test_case000 import Case

#if __name__ == '__main__':



#    r = report()
#    r.make_report()
#    filename = r.get_reportName()

#    s = sendEmail()
#    s.send_mail(filename)

#    l = Log()
#    l.log_debug("debug message")
#    l.log_info("info message")
#    l.log_warn("warn message")
#    l.log_error("error message")

#    print(datetime.now().strftime("%Y-%m-%d %H_%M_%S"))
#    fd = readConf('Test.ini')
#    val = fd.get_data('TEST', 'name')
#    print(val)

 #   fd = readExcel('Test.xlsx')
 #   str = fd.get_value('Test', 0)
 #   print(str)

#    Test = MainStart()
#    Test.test_main()