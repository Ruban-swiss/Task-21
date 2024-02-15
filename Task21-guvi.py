from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class Task21:

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
        username_input= self.driver.find_element(by=By.NAME, value="email")
        password_input = self.driver.find_element(by=By.NAME, value="password")

        username_input.send_keys("ruban19@gmail.com")
        password_input.send_keys("Ru&790734")

        self.driver.find_element(by=By.TAG_NAME, value="button").click()

        sleep(10)
        
    def getURL(self):
        return self.driver.current_url

    def getCookies(self):
        return self.driver.get_cookies()
    
    def logout(self):
         xpath = '/html/body/div[1]/nav/div/div/div/div/button[2]'
        Logout_button = self.driver.find_element(by=By.XPATH, value=xpath)
        Logout_button.click()

url = "https://www.zenclass.in/dashboard"
obj = Task21(url)
obj.boot()
print(obj.getCookies())
obj.login()
print(obj.getCookies())
print(obj.getURL())
obj.logout()
obj.quit()
