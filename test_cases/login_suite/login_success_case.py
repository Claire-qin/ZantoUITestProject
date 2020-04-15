#测试禅道的登录完整的流程  selenium+unittest+报告
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver
from common import login

class LoginSuccessCase(unittest.TestCase):
    def setUp(self):
        self.driver =set_driver.set_driver()

    def tearDown(self): #清理 还原
        time.sleep(1)
        self.driver.quit()

    def test_login_1(self):
        '''case01 使用admin  admin123456测试能否登录'''
        login.login(self.driver,'admin','admin123456')
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH,'//span[@class="user-name"]'),'admin'),'test_login测试执行失败')

    def test_login_2(self):
        '''case02 使用test01  admin123456测试能否登录'''
        login.login(self.driver, 'test01', 'admin123456')
        actual_result = self.driver.find_element(By.XPATH,'//span[@class="user-name"]').text
        self.assertEqual(actual_result,'测试人员1','test_login_2测试执行失败')

if __name__ == '__main__':
    unittest.main(verbosity=2)

