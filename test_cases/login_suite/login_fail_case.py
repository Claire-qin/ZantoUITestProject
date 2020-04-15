#测试禅道的登录完整的流程  selenium+unittest+报告
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver
from common import login

class LoginFailCase(unittest.TestCase):
    def setUp(self):  # 初始化配置
        self.driver = set_driver.set_driver()

    def tearDown(self): #清理 还原
        time.sleep(1)
        self.driver.quit()

    def test_login(self):
        '''case03 使用admin  admin12345测试能否登录'''
        login.login(self.driver, 'admin', 'admin12345')
        self.assertTrue(WebDriverWait(self.driver,10).until(EC.alert_is_present())) #返回文本框内容

if __name__ == '__main__':
    unittest.main()

