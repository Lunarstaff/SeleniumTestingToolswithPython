# searchproduct.py


from selenium import webdriver
import os

# 创建一个新的IE浏览器会话
ie = webdriver.Ie()
ie.implicitly_wait(30)
ie.maximize_window()

# 打开主页
#https://zhi.hao123.com/
ie.get("https://zhi.hao123.com/")

# 获取输入搜索文本的框框（控件）
search_text = ie.find_element_by_name("wd")
search_text.clear()

# 键入搜索关键字文本，并提交
search_text.send_keys("游戏")
search_text.submit()

# 获取所以产品名称的元素
# 使用 find_elements_by_xpath 方法
products = ie.find_element_by_xpath("//span[@class=‘H’]/a")

# 打印获取到的产品数目
print("找到了{}产品名称包含游戏的产品。".format(str(len(products))))

# 遍历并打开出产品
with open("../searchproduct.txt","a+") as p:
    for i in products:
        p.write(i)
    p.close()

# 关闭浏览器
ie.close()
