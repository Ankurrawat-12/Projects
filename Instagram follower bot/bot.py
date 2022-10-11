from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

SIMILAR_ACCOUNT = ""
USERNAME = ""
PASSWORD = ""
chrome_driver_path = r"D:\Development\chromedriver.exe"


class Bot:

    def __init__(self):
        self.brave = webdriver.chrome.options.Options()
        self.brave.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=self.brave)

    def log_in(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        sleep(3)
        password.send_keys(Keys.ENTER)
        sleep(6)
        # close_popup1 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        # close_popup1.click()
        # close_popup = self.driver.find_element_by_css_selector('.mt3GC .HoLwm')
        # close_popup.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        sleep(6)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(4)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(50):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        sleep(2)
        a = 0
        for button in all_buttons:
            try:
                button.click()
                a += 1
                print(a)
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_css_selector(".mt3GC .HoLwm")
                cancel_button.click()
