# find_method_test.py
import unittest
from selenium import webdriver
import os
import os.path

class AC10_reviews_load(unittest.TestCase):

    def test_Elements_Ineed(self):
        self.ie = webdriver.Ie()
        self.ie.implicitly_wait(30) # 隐式等待30s
        self.ie.maximize_window()   # 窗口最大化

        self.ie.get("https://item.jd.com/5448880.html")  # 打开AC0产品页面
        # pingjia_Num = self.ie.find_element_by_xpath("//em[@class='J_ReviewsCount']")
        button_pingjia = self.ie.find_element_by_xpath("//li[@data-anchor='#comment']")
        button_pingjia.click()
        os.chdir("C:\\E-Data-File\\腾讯课堂\\Python入门\\SeleniumTestingToolswithPython\\Chapter3\\testcode")
        with open("AC10_Reviews.txt", "w") as AC10output:
            while True:
                self.ie.execute_script("var q=document.documentElement.scrollTop=100000")
                reviews_in_page = self.ie.find_elements_by_xpath("//div[@class='comment-item']")
                try:
                    for i in reviews_in_page:
                        review_order_info = i.find_element_by_class_name("order-info").text
                        review_i = i.find_element_by_class_name("comment-con").text
                        review_user = i.find_element_by_class_name("user-info").text
                        AC10output.write("评论用户信息：" + review_user + "###" + "\n")
                        AC10output.write("用户定单信息：" + review_order_info + "\n")
                        AC10output.write("###" + review_i + "###\n")
                        AC10output.write("#".center(60, "#") + "\n")
                    print("写入完成！")
                    try:
                        button_nextPage = self.ie.find_element_by_xpath("//a[@class='ui-page-next' href='#comment']")
                        button_nextPage.click()
                    except:
                        print("翻页失败！")
                        break
                except:
                    print("写入失败！")
        AC10output.close()

    def tearDown(self):
        # 关闭浏览器
        self.ie.quit()

if __name__ == "__main__":
    unittest.main()