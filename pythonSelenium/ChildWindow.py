
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\Pc\\PycharmProjects1\\ChromeDriver\\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element_by_link_text("Click Here").click()

childwindow = driver.window_handles[1]
parentwindow = driver.window_handles[0]
# (" parentid "," chlidid ")
driver.switch_to.window(childwindow)
print(driver.find_element_by_tag_name("h3").text)
print("The above given is the child window text!!!")
driver.close()
driver.switch_to.window(parentwindow)
assert "Opening a new window" == driver.find_element_by_tag_name("h3").text
# print("The above given is the Parent window text!!!")
