from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# url = "https://en.wikipedia.org/wiki/Main_Page"
url = "https://secure-retreat-92358.herokuapp.com/"
chrome_driver_path = r"D:\Development\chromedriver.exe"

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
brave = webdriver.chrome.options.Options()
brave.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=brave)
driver.get(url)
""""
article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)
# article_count.click()

all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name("search")
search.se("Python")
search.send_keys(Keys.ENTER)
"""

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Ankur")
first_name.send_keys(Keys.ENTER)
second_name = driver.find_element_by_name("lName")
second_name.send_keys("Rawat")
second_name.send_keys(Keys.ENTER)
email = driver.find_element_by_name("email")
email.send_keys("ankurrawat620@gmail.com")
email.send_keys(Keys.ENTER)
button = driver.find_element_by_class_name("btn-primary")
button.click()
driver.quit()
