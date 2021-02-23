# invoke chrome browser (select Chrome class)
# browser exposes an executable file
# through selenium test we need to invoke executable file which will then invoke actual browser
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Pc\\PycharmProjects1\\ChromeDriver\\chromedriver.exe")


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# for radio buttons also we can use find ELEMENTS
RadioButtons = driver.find_elements_by_xpath("//input[@name='radioButton']")
RadioButtons[2].click()
RadioButtons[2].is_selected()

assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()