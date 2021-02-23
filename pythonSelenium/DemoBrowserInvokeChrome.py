
# how to invoke a browser in python selenium
from threading import Thread
from selenium import webdriver


# invoke chrome browser (select Chrome class)
# browser exposes an executable file
# through selenium test we need to invoke executable file which will then invoke actual browser

driver = webdriver.Chrome(executable_path="C:\\Users\\Pc\\PycharmProjects1\\ChromeDriver\\chromedriver.exe")
driver.maximize_window()  # to maximise window
driver.get("https://rahulshettyacademy.com/#/index") # to navigate to any url
driver.title  # to extract the title
print(driver.title)  # to print the title on output
print(driver.current_url)  # to get the current url
driver.get("https://rahulshettyacademy.com/#/consulting")
driver.back()  # to come back to old site
driver.refresh()  # to refresh
driver.minimize_window()  # to minimise window

driver.close()  # to close the browser that got invoked current window
# driver.quit()  # to quit all the the browser that got invoked


