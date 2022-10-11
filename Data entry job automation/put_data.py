from selenium import webdriver
from time import sleep

url = "https://docs.google.com/forms/d/e/1FAIpQLSdiOecMALiYKYOTwQqqExiHjXLaar-3zJoRoBlcqiCRDrxqAA/viewform?usp=sf_link"

chrome_driver_path = r"D:\Development\chromedriver.exe"


class PutData:
    def __init__(self):
        self.brave = webdriver.chrome.options.Options()
        self.brave.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=self.brave)

    def open_forms(self):
        self.driver.get(url)

    def fill_form(self, a_list, p_list, l_link):
        for i in range(len(a_list)):
            address = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
            address.send_keys(a_list[i])
            price.send_keys(p_list[i])
            link.send_keys(l_link[i])
            submit.click()
            another_response = self.driver.find_element_by_link_text("Submit another response")
            another_response.click()
            sleep(2)
        self.driver.close()
