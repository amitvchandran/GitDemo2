#  Implicit  wait and Explicit wait
# also using time class
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions


list = []
list2= []
driver = webdriver.Chrome(executable_path="C:\\Users\\Pc\\PycharmProjects1\\ChromeDriver\\chromedriver.exe")


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)

count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")


# //div[@class='product-action']/button/parent::div/parent::div/h4
# the above is the general expression to traverse to above parent from child

for i in buttons:
    list.append(i.find_element_by_xpath("parent::div/parent::div/h4").text)
    i.click()
print(list)

driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 6)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))

veggies = driver.find_elements_by_xpath("//p[@class='product-name']")
for veg in veggies:
    list2.append(veg.text)
print(list2)
assert list == list2

originalAmt = driver.find_element_by_css_selector("span.discountAmt").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
discountAmt = driver.find_element_by_css_selector("span.discountAmt").text
assert float(discountAmt) < int(originalAmt)

print(driver.find_element_by_css_selector(".promoInfo").text)

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)  # Ist iteration sum 0+32+48+60

print(sum)
totalAmt = int(driver.find_element_by_class_name("totAmt").text)
assert sum == totalAmt
