from selenium import webdriver

chrome_driver_path = r"D:\Development\chromedriver.exe"

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
options = webdriver.chrome.options.Options()
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
# driver.get("https://www.amazon.in/gp/product/1421525828/ref=ox_sc_saved_title_6?smid=AWKKPKP4FBRXQ&psc=1")
# price = driver.find_element_by_class_name("a-size-medium")
# print(price.text)
# driver.get("https://python.org")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)
# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)
# driver.find_elements_by_css_selector()
# # driver.close()

# driver.quit()

dictionary = {}
driver.get("https://python.org")
title = driver.find_elements_by_css_selector(".event-widget li a")
date = driver.find_elements_by_css_selector(".event-widget li time")

for n in range(len(title)):
    dictionary[n] = {
            'time': date[n].text,
            'name': title[n].text
    }

print(dictionary)

driver.quit()
