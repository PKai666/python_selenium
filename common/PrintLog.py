import logging
import os
from datetime import datetime

LOGPATH = '\logging'

class Log:
    def __init__(self):
        self.cur_path = os.path.dirname(os.path.realpath(__file__))
        self.real_path = self.cur_path + LOGPATH

        if not os.path.exists(self.real_path):
            os.mkdir(self.real_path)
        self.handler = logging.FileHandler(os.path.join(self.real_path,
                                                   '%s.log'%(datetime.now().strftime('%Y-%m-%d %H-%M'))))

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)



    def log_debug(self, msg):
        self.logger.debug(msg)
        self.logger.removeHandler(self.handler)
    def log_info(self, msg):
        self.logger.info(msg)
        self.logger.removeHandler(self.handler)
    def log_warn(self, msg):
        self.logger.warn(msg)
        self.logger.removeHandler(self.handler)
    def log_error(self, msg):
        self.logger.error(msg)
        self.logger.removeHandler(self.handler)