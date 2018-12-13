from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from common.PrintLog import Log
import unittest
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def WebDriver_Wait(driver, times, func):
    return WebDriverWait(driver, times).until(func)

url = 'http://www.baidu.com'

class Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(url)
        cls.driver.maximize_window()
#        self.driver.implicitly_wait(3)
#        Log().log_info('init webpage sucess')
    @classmethod
    def tearDownClass(cls):
        pass

    def test_1(cls):
        cls.driver.implicitly_wait(2)
        move = cls.driver.find_element_by_link_text('新闻')
        ActionChains(cls.driver).move_to_element(move).click().perform()

        co = cls.driver.get_cookies()
        print(co)
        cls.driver.delete_cookie('domain')
        cl = cls.driver.get_cookies()
        print(cl)


#       滚动条
#       js = 'var q = document.documentElement.scrollTop=20000'
 #       cls.driver.execute_script(js)
#        sleep(2)
#        js1 = 'var q = document.documentElement.scrollTop=0'
#        cls.driver.execute_script(js1)

#       键盘事件
#       mov = cls.driver.find_element_by_link_text('新闻').send_keys(Keys.CONTROL, 'a')


#if __name__ == '__main__':
 #   unittest.main()

