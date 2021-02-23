
# invoke chrome browser (select Chrome class)
# browser exposes an executable file
# through selenium test we need to invoke executable file which will then invoke actual browser
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Pc\\PycharmProjects1\\ChromeDriver\\chromedriver.exe")
driver.maximize_window()  # to maximise window

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("ind")
# introduce sleep since there is a delay for autosuggestion to come
time.sleep(2)  # for 2 seconds
# use find elements (plural) to get every common stuff in the list
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
# to know the length or count of countries
print(len(countries))
# use for loop to iterate
for country in countries:
    if country.text == "India":
        country.click()
        break
print(driver.find_element_by_id("autosuggest").text)
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"


