from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\Pc\\PycharmProjects1\\ChromeDriver\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_xpath("//a[contains(@href,'/shop')]").click()

products = driver.find_elements_by_xpath("//div[@class='card h-100']")


# //div[@class='card h-100']/div/h4/a
# product = //div[@class='card h-100']
# //div[@class='card h-100']/div[2]/button
for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
        # Add Items to cart
        product.find_element_by_xpath("div[2]/button").click()

driver.find_element_by_xpath("//a[contains(@class,'btn-primary')]").click()
driver.find_element_by_xpath("//button[contains(@class,'btn-success')]").click()

driver.find_element_by_id("country").send_keys("ind")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class= 'checkbox checkbox-primary']").click()
driver.find_element_by_xpath("//input[@type= 'submit']").click()
print(driver.find_element_by_class_name("alert-success").text)


