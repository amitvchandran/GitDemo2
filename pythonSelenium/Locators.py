from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\Pc\\PycharmProjects1\\ChromeDriver\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_xpath("/html/body/app-root/form-comp/div/h4/input").send_keys("Amit Chandran")
#driver.find_element_by_xpath("//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[1]/input[1]").send_keys("Amit")
#driver.find_element_by_class_name("email").send_keys("email.com")
#driver.find_element_by_id("exampleCheck1").click()
#driver.find_element_by_xpath("//input[@type='submit']").click()

# regular Expressions
# [class*='alert-success']   ::this is for CSS
# //*[contains(@class,'alert-success')]   :: this is for Xpath