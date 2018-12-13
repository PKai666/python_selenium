from common.ReadConfig import readConf
from common.PrintLog import Log
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
from email.utils import formataddr
from email import encoders
import os
import smtplib


SECTION='EMAIL'
FILENAME='Test.ini'
REPORTPATH=r'./report'

class sendEmail:
    def __init__(self):
        config = readConf(FILENAME)
        self.smtp_server = config.get_data(SECTION, 'smtp')
        self.smtp_port = config.get_data(SECTION, 'port')
        self.sender = config.get_data(SECTION, 'sender_account')
        self.pwd = config.get_data(SECTION, 'send_pwd')
        self.receiver = config.get_data(SECTION, 'receiver')
        self.subject = config.get_data(SECTION, 'subject')
        self.content = config.get_data(SECTION, 'content_text')

    def send_mail(self,reportname):
        self.msg = MIMEMultipart()
        self.msg['From'] = formataddr(['Test', self.sender])
        self.msg['To'] = formataddr(['Test', self.receiver])
        self.msg['Sbuject'] = Header(self.subject, 'UTF-8')
        self.msg.attach(MIMEText('%s'% self.content,'plain', 'UTF-8' ))
#        self.curr_path = os.path.dirname(os.path.realpath(__file__))
#        self.report_path = self.curr_path + REPORTPATH
        self.report_path = os.path.abspath(REPORTPATH)
        self.html = os.path.join(self.report_path,
                                 '%s.html'% reportname)


        with open(self.html, 'rb') as f:
            self.docu = MIMEBase('html', 'html', filename='report.html')
            self.docu.add_header('Content-Disposition', 'attachment', filename='report.html')
            self.docu.add_header('Content-ID', '<0>')
            self.docu.add_header('X-Attachment-Id', '0')
            self.docu.set_payload(f.read())
            encoders.encode_base64(self.docu)
        self.msg.attach(self.docu)

        try:
            server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
            server.login(self.sender, self.pwd)
            server.sendmail(self.sender, [self.receiver], self.msg.as_string())
            server.quit()
            Log().log_info('send success')
        except:
            Log().log_info('send false')






