import sys, pytest
from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver
sys.path.append("D:\Program Files\py")

from base.base import Base
from base import init_driver


class Test:
    def setup_class(self):
        # 获取driver
        self.driver = init_driver.p_driver()
        self.base = Base(self.driver)
        self.driver.get("https://gov.jlb.47.jlb0.uidev.work")

    def test_1(self):
        self.base.input_ele((By.ID, "user-name"), "admin")
        self.base.input_ele((By.ID, "user-pwd"), "admin")
        sleep(3)
        self.base.click_ele((By.ID,"LoginButton"))


    # def test_2(self):
    #     driver = webdriver.Chrome()
    #     el= driver.find_element()
    #     el.click()
    def teardown_class(self):
        self.driver.quit()

