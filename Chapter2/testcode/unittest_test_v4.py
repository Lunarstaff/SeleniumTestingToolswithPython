# unittest_test_v3.py
import unittest
import HTMLTestRunner
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# 动漫套图https://www.aitaotu.com/dmtp/


class taotuTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # 创建一个IE浏览器进程
        cls.driver = webdriver.Ie()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # 打开指定的网址
        cls.driver.get("https://www.aitaotu.com/dmtp/")

    def test_search_field(self):
        # 检查界面上是否有 录入搜索关键词的文本框
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    def test_search_button(self):
        # 检查界面上是否有 搜索按钮
        self.assertTrue(self.is_element_present(By.ID, "ssubmit"))

    def test_firstpage_date(self):
        # 检查首面上最新更新日期
        first_page = self.driver.find_element_by_link_text("首页")
        first_page.click()
        update_date = self.driver.find_element_by_class_name("date")
        self.assertEqual(update_date.text, "DATE12-07")

    @classmethod
    def tearDown(cls):
        # 关闭浏览器窗口
        cls.driver.quit()

    # 测试套件：
    def is_element_present(self, how, what):
        """

        :param how:
        :param what:
        :return:
        """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    if __name__ == "__main__":
        unittest.main(verbosity=2)


dir = os.getcwd()  # 报告输出目录
outfile = open(dir + "\\testreport.html", "w")  # 打开测试报告文件
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title="TestReport", description="Taotu")  # 配置
runner.run(taotuTest)


