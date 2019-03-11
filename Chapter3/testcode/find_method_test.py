# find_method_test.py
import unittest
from selenium import webdriver


class Find_Element_Test(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # 创建一个IE浏览器会话进程
        cls.ie = webdriver.Ie()
        cls.ie.implicitly_wait(30) # 隐式等待30s
        cls.ie.maximize_window()   # 窗口最大化

    def test_search_button_enabled(self):
        # 测试百度主页搜索按钮可用
        self.ie.get("https://www.baidu.com/")
        # 获取搜索按钮
        search_button = self.ie.find_element_by_class_name("s_btn")

        # 检查搜索按钮是否可用
        self.assertTrue(search_button.is_enabled())

    def test_search_tagname(self):
        self.ie.get("https://www.baidu.com/")
        # 获取所有的ur标签
        ele_script = self.ie.find_elements_by_tag_name("script")
        print("script标签有{}个".format(len(ele_script)))

    def test_xpat_search(self):
        self.ie.get("https://detail.tmall.com/item.htm?spm=a1z10.5-b-s.w4011-14445208949.68.5f13a0e9sn1ukV&id=559262362075&rn=e5615e473665193c98648c2b8e4dcce2&abbucket=15&sku_properties=5919063:33030646")
        pingjia = self.ie.find_element_by_xpath("//a[@href='#J_Reviews']")
        pingjiaNum = self.ie.find_element_by_xpath("//em[@class='J_ReviewsCount']")
        self.assertEqual(pingjia.text, "累计评价 " + pingjiaNum.text)


    #def tearDown(self):
        # 关闭浏览器
        #self.ie.quit()

if __name__ == "__main__":
    unittest.main()