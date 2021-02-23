# JSE DOM can access any  element in web page just like selenium does
# selenium have the method to execute JS code in it

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Pc\\PycharmProjects1\\ChromeDriver\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute("value"))
# using JSE execute script, selenium gives control to JS
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

# to click any element using JSE
shopButton = driver.find_element_by_xpath("//a[@href='/angularpractice/shop']")

# using JSE to click use arguments.click()
driver.execute_script('arguments[0].click();', shopButton)

# selenium does not know how to scroll down
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

