import sys,pytest
sys.path.append("D:\Program Files\py")

from base.base import Base

class Test:
    def setup_class(self):
        base = Base()
        self.driver = base.driver

    def test_1(self):
        self.driver.get("http://www.baidu.com")

    def test_2(self):
        self.driver.get("http://www.qq.com")
    def teardown_class(self):
        self.driver.quit()


