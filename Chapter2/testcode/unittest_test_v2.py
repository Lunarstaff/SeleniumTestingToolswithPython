# unittest_test_v2.py
import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 创建一个浏览器实例
        cls.driver = webdriver.Ie()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # 导航
        cls.driver.get("http://www.baidu.com")
        cls.driver.title

    def test_search_by_category(self):
        # 获取搜索框元素
        # 录入关键字
        # 获取所以指定标签的元素
        # 。。。
        self.assertEqual("预期结果1", "实际结果1")

    def test_search_by_name(self):
        # 获取搜索框元素
        # 录入关键字
        # 获取所以指定标签的元素
        self.assertEqual("预期结果2", "实际结果2")

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

