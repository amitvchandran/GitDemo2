from selenium import webdriver
from selenium.webdriver.support.select import Select

# opt.add_argument("--disable-web-security")
# opt.add_argument("--allow-running-insecure-content")
# opt.add_argument("--no-sandbox")
# opt.add_argument("--disable-setuid-sandbox")
# opt.add_argument("--disable-webgl")
# opt.add_argument("--disable-popup-blocking")
# options.add_argument("headless")
# options.add_argument("window-size=1500,1200")
# options.add_argument("no-sandbox")
# options.add_argument("disable-dev-shm-usage")
# options.add_argument("disable-gpu")
# options.add_argument("log-level=3")
# options.add_argument(f"user-agent={userAgent}")





chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
# for certification errors accept like SSL
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path="C:\\Users\\Pc\\PycharmProjects1\\ChromeDriver\\chromedriver.exe", options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
