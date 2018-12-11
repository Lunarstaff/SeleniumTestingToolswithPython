# taobao_v1.py
import unittest as ut
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


# 【商品搜索测试】： 打开taobao首页并搜索 商品“糖”。
class GoodsSearchTest(ut.TestCase):
    @classmethod
    def setUp(cls):
        # 创建浏览器进程
        cls.driver = webdriver.Ie()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # 打开taobao首页
        cls.url = "https://www.taobao.com/"
        cls.driver.get(cls.url)

    def test_search_field(self):
        # 检查首页上是否有搜索框
        search_button = self.driver.find_element_by_id("q")
        self.assertTrue(search_button)

    def test_mytaobao(self):
        # 检查首页上是否有“我的淘宝”入口
        myTaobao = self.driver.find_element_by_id("J_SiteNavMytaobao")
        self.assertTrue(myTaobao)

    @classmethod
    def tearDown(cls):
        # 关闭浏览器
        cls.driver.quit()


if __name__ == "__main__":
    ut.main(verbosity=2)
