'''
Created on Nov 7, 2018

@author: SESA505977
'''

from selenium import webdriver
# class openingbrowser:
#     def browser(self):
#         url="http://www.gmail.com"
#         driver=webdriver.Chrome()
#         driver.set_page_load_timeout(30)
#         driver.get(url)
#         driver.maximize_window()
#         driver.find_element_by_id("identifierId").send_keys("anil.python7@gmail.com")
#         driver.find_element_by_class_name("CwaK9").click()
#         driver.find_element(by, value)("Xb9hP").send_keys("anilreddy76")
#         driver.find_element_by_class_name("CwaK9").click()
#         driver.save_screenshot("gmail.png")
# #driver.quit()
# ob=openingbrowser()
# ob.browser()

class FindByIdName():

    def test(self):
        baseUrl = "http://ci2preprod.westeurope.cloudapp.azure.com:8081"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.find_element_by_xpath('//*[@class="auth0-lock-tabs-current"]/..//*[contains(text(),"Log In")]')

#         if elementById is None:
#             print("We not found an element by Id")
# 
#         elementByName = driver.find_element_by_name("show-hide")
# 
#         if elementByName is None:
#             print("We not found an element by Name")

ff = FindByIdName()
ff.test()