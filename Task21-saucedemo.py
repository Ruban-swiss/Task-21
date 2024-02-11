from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class Task20:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(10)

    def quit(self):
        self.driver.quit()

    def login(self):
        username_input= self.driver.find_element(by=By.ID, value="user-name")
        password_input = self.driver.find_element(by=By.ID, value="password")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")

        self.driver.find_element(by=By.ID, value="login-button").click()

        sleep(10)
        
    def getURL(self):
        return self.driver.current_url

    def getCookies(self):
        return self.driver.get_cookies()

url = "https://www.saucedemo.com/"
obj = Task20(url)
obj.boot()
print(obj.getCookies())
obj.login()
print(obj.getCookies())
print(obj.getURL())
obj.quit()