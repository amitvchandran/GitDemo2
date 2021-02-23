
# how to invoke a browser in python selenium
from select import select
from threading import Thread
from selenium import webdriver


# invoke chrome browser (select Chrome class)
# browser exposes an executable file
# through selenium test we need to invoke executable file which will then invoke actual browser
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Pc\\PycharmProjects1\\ChromeDriver\\chromedriver.exe")
driver.maximize_window()  # to maximise window
driver.get("https://rahulshettyacademy.com/angularpractice/") # to navigate to any url
# to select the static drop down use select class

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

