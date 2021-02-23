# invoke chrome browser (select Chrome class)
# browser exposes an executable file
# through selenium test we need to invoke executable file which will then invoke actual browser
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Pc\\PycharmProjects1\\ChromeDriver\\chromedriver.exe")
driver.maximize_window()  # to maximise window

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# to get and click the checkbox we use find elements and iterate through for loops to get the desired task done
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()