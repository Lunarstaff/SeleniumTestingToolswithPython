# unittest_test_v1.py

import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):
    def setUp(self):
        # 创建一个IE浏览器会话进程
        self.ie = webdriver.Ie()
        self.ie.implicitly_wait(30) # 隐式等待30s
        self.ie.maximize_window()   # 窗口最大化

    def test_search_ticket_001(self):
        # 打开指定的URL
        ticket_search_url = "https://kyfw.12306.cn/otn/leftTicket/init"     # 余票查询
        self.ie.get(ticket_search_url)

        # 找到出发地录入框："上海:SHH"
        self.from_p = self.ie.find_element_by_id("fromStationText")
        self.from_p.click()
        self.button_SHH = self.ie.find_elements_by_xpath("//li[@data='SHH']")
        self.button_SHH[0].click()
        # 找到出发地录入框："深圳:SZQ"
        self.to_p = self.ie.find_element_by_id("toStationText")
        self.to_p.click()
        self.button_SZQ = self.ie.find_elements_by_xpath("//li[@data='SZQ']")
        self.button_SZQ[0].click()

        # 查询
        self.search_button = self.ie.find_element_by_id("query_ticket")
        self.search_button.click()

        # 定位车次列表并检查
        trains = self.ie.find_elements_by_xpath("//a[@title='点击查看停靠站信息']")
        for i in trains:
            self.assertEqual("D2287", i.text)
            break

    def test_iqiyi_search_001(self):
        self.url_iqiyi = 'http://www.iqiyi.com/'
        self.ie.get(self.url_iqiyi)
        self.iqiyi_search = self.ie.find_element_by_id("nav_searchboxIn")
        self.iqiyi_search.send_keys("让子弹飞一会儿").submit()

    def tearDown(self):
        # 关闭浏览器
        self.ie.quit()

if __name__ == "__main__":
    unittest.main()