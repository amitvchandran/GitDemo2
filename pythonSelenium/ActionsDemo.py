
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Pc\\PycharmProjects1\\ChromeDriver\\chromedriver.exe")
# Mouse hover
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#action = ActionChains(driver)
#menu = driver.find_element_by_id("mousehover")
#action.move_to_element(menu).perform()
#Childmenu = driver.find_element_by_link_text("Top")
#action.move_to_element(Childmenu).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.double_click(driver.find_element_by_id("double-click")).perform()
alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()

