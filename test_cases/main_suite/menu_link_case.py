import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver
from common import login

class MenuLinkCase(unittest.TestCase):
    def setUp(self):  # 初始化配置
        self.driver =set_driver.set_driver()
        login.login(self.driver, 'admin', 'admin123456')

    def tearDown(self): #清理 还原
        time.sleep(1)
        self.driver.quit()

    def test_my_link(self):
        '''case04 验证【我的地盘】菜单能否正确链接'''
        self.driver.find_element(By.XPATH, '//li[@data-id="my"]').click()
        self.assertTrue(EC.title_is('我的地盘 - 禅道'))

    def test_product_link(self):
        '''case05 验证【产品】菜单能否正确链接'''
        self.driver.find_element(By.XPATH, '//li[@data-id="product"]').click()
        self.assertTrue(EC.title_is('产品主页 - 禅道'))

    def test_company_link(self):
        ''' case06 验证【组织】菜单能否正确链接'''
        self.driver.find_element(By.XPATH,'//a[@href="/zentao/company/"]').click()
        self.assertTrue(EC.title_is('组织视图首页-部门结构 - 禅道'))

if __name__ == '__main__':
    unittest.main()

