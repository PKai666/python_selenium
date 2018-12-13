import configparser
from configparser import ConfigParser
import os

class readConf:
    def __init__(self,filename):
        self.cur_path = os.path.dirname(os.path.realpath(__file__))
        self.ini_path = os.path.join(self.cur_path, filename)
        self.file = ConfigParser()
        self.file.read(self.ini_path)

    def get_data(self, section, key):
        return self.file.get(section, key)

    def set_date(self, section, key, value):
        with open(self.file, 'w') as fp:
            self.file.set(section, key, value)
            self.file.write(fp)
        fp.close()
