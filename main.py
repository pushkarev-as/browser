from selenium import webdriver
from selenium.webdriver.firefox.options import Options

if __name__ == '__main__':
    try:
        print('Начало работы')
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
        driver.fullscreen_window()
        driver.get('https://ya.ru')
        print(f'Название сайта: {driver.title}')
    except Exception as err:
        print(err)
    finally:
        driver.close()
        driver.quit()
