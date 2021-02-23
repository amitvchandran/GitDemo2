from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\Pc\\PycharmProjects1\\ChromeDriver\\chromedriver.exe")

driver.get("https://login.salesforce.com/?locale=in")

# for generating CSS from ID you can use    "tagname#ID"
# for generating CSS from Classname you can use  "tagname.classname"
driver.find_element_by_css_selector("#username").send_keys("Amit")
driver.find_element_by_css_selector(".password").send_keys("chandran")
# if i want to clear the input in edit box
driver.find_element_by_css_selector(".password").clear()
# locators using link text (only when tagname is a)
driver.find_element_by_link_text("Forgot Your Password?").click()
# for finding by text using Xpath
# //tagname[text()='xyz']
driver.find_element_by_xpath("//a[text()='Cancel']").click()
# to get label "username" by xpath
print(driver.find_element_by_xpath("//form[@id='login_form']/div/label").text)
# to get label "password" by css
print(driver.find_element_by_css_selector("form[id='login_form'] label:nth-child(4)").text)

