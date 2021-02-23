
# how to invoke a browser in python selenium
from select import select
from threading import Thread
from selenium import webdriver


# invoke chrome browser (select Chrome class)
# browser exposes an executable file
# through selenium test we need to invoke executable file which will then invoke actual browser
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Pc\\PycharmProjects1\\ChromeDriver\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\Users\\Pc\\PycharmProjects1\\FirefoxDriver\\geckodriver.exe")
driver.maximize_window()  # to maximise window
driver.get("https://rahulshettyacademy.com/angularpractice/") # to navigate to any url
# to select the static drop down use select class

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

# ASSERTION always expects to return TRUE

driver.find_element_by_xpath("//input[@type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)

# now we use assert

message = driver.find_element_by_class_name("alert-success").text

assert "Success!" in message  #if Success! text is present it will return true else false
