from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class Base():
    def __init__(self,driver):
        self.driver = driver

    def find_element(self, loc, time=5, fc=0.5):
        by = loc[0]
        path = loc[1]
        if by == By.XPATH:
            path = self.make_xpath(path)
        return WebDriverWait(self.driver, time, fc).until(lambda x: x.find_element(by, path))

    def input_ele(self,loc,text):
        el=self.find_element(loc)
        el.clear()
        el.send_keys(text)

    def click_ele(self,loc):
        el=self.find_element(loc)
        print(el)
        el.click()


    def make_xpath(self, loc):
        feature_start = "//*["
        feature_end = "]"
        feature = ''

        if isinstance(loc,str):
            if loc.startswith("//"):
                return loc
            else:
                for i in loc:
                    feature+= self.make_xpath_unit(i)
        feature = feature.strip("and ")
        loc = feature_start +feature+feature_end
        return loc

    def make_xpath_unit(self,loc):
        """
                拼接xpath中间的部分
                :param loc:
                :return:
                """
        key_index = 0
        value_index = 1
        option_index = 2

        args = loc.split(",")
        feature = ""

        if len(args) == 2:
            feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "
        elif len(args) == 3:
            if args[option_index] == "1":
                feature = "@" + args[key_index] + "='" + args[value_index] + "'" + "and "
            elif args[option_index] == "0":
                feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "

        return feature
