from selenium.webdriver.common.by import By

from base.base import Base

class Login(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    def login(self):
        self.input_ele((By.ID,"user-name"))

