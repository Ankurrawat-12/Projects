from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

url = "https://www.linkedin.com/jobs/search/"

chrome_driver_path = r"D:\Development\chromedriver.exe"

brave = webdriver.chrome.options.Options()
brave.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=brave)
driver.get(url)

time.sleep(2)
sign_in = driver.find_element_by_class_name("nav__button-secondary")
sign_in.click()
time.sleep(5)
username = driver.find_element_by_id("username")
username.send_keys("ankurrawat2c6rcitt@gmail.com")
username.send_keys(Keys.ENTER)
password = driver.find_element_by_id("password")
password.send_keys("A@nkur123")
password.send_keys(Keys.ENTER)
time.sleep(5)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(8287413412)

        submit_button = driver.find_element_by_css_selector("footer button")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
