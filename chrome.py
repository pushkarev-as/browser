from selenium import webdriver

# options
options = webdriver.ChromeOptions()

# headless mode
# options.add_argument("--headless")
# options.headless = True
options.add_argument("start-maximized")
# options.add_argument("--disable-blink-features=AutomationControlled")
try:
    driver = webdriver.Chrome(
        # executable_path="/home/cain/PycharmProjects/selenium_python/chromedriver/chromedriver",
        options=options
    )
    driver.get('https://ya.ru')
    print('Work!')
except Exception as error:
    print(error)

input('?')