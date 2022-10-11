from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

url = "https://www.speedtest.net/"
url2 = "https://twitter.com/login"
chrome_driver_path = r"D:\Development\chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.brave = webdriver.chrome.options.Options()
        self.brave.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=self.brave)
        self.driver.fullscreen_window()
        self.download_speed = 0
        self.upload_speed = 0
        self.msg = f"Hey internet provider,why is my internet speed {self.download_speed}down/" \
                   f"{self.upload_speed}up when i pay for 100down/10up?"

    def get_internet_speed(self):
        self.driver.get(url)
        go = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()

        try:
            sleep(60)
            self.download_speed = self.driver.find_element_by_xpath(
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
            self.upload_speed = self.driver.find_element_by_xpath(
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        except NoSuchElementException as a:
            print(a)
            print("element not found. Trying again")
            sleep(20)
            self.download_speed = self.driver.find_element_by_xpath(
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
            self.upload_speed = self.driver.find_element_by_xpath(
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(self.download_speed)
        print(self.upload_speed)
        # self.driver.close()

    def tweet_at_provider(self):
        self.driver.get(url2)
        print("twitter")
        sleep(10)
        username = self.driver.find_element_by_name("session[username_or_email]")
        username.send_keys("ankurrawatc6rcitt@gmail.com")
        username.send_keys(Keys.ENTER)
        password = self.driver.find_element_by_name("session[password]")
        password.send_keys("+5$5EvX!Y+PLyNI")
        password.send_keys(Keys.ENTER)
        log_in = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
        log_in.click()
        sleep(20)
        tweeter_message = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div')
        tweeter_message.send_keys(self.msg)
        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet.click()
        sleep(10)
        self.driver.quit()
