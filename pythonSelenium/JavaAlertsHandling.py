# invoke chrome browser (select Chrome class)
# browser exposes an executable file
# through selenium test we need to invoke executable file which will then invoke actual browser
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

validateText = "Option3"
validateText1 = "Amit"

driver = webdriver.Chrome(executable_path="C:\\Users\\Pc\\PycharmProjects1\\ChromeDriver\\chromedriver.exe")


driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_xpath("//input[@name='enter-name']").send_keys("Option3")
driver.find_element_by_xpath("//input[@id='alertbtn']").click()
# for JavaAlerts we have to SwitchTo
Alert = driver.switch_to.alert
AlertText = Alert.text
assert validateText in AlertText
Alert.accept()  # this will accept the alert (click OK)

time.sleep(3)

driver.find_element_by_xpath("//input[@name='enter-name']").send_keys("Amit")
driver.find_element_by_xpath("//input[@id='alertbtn']").click()
# for JavaAlerts we have to SwitchTo
Alert = driver.switch_to.alert
AlertText = Alert.text
assert validateText1 in AlertText
Alert.dismiss()  # if we want to cancel/ Click NO to an Alert button