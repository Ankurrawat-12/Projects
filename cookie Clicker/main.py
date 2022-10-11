from selenium import webdriver
import time

url = "https://orteil.dashnet.org/cookieclicker/"

chrome_driver_path = r"D:\Development\chromedriver.exe"

brave = webdriver.chrome.options.Options()
brave.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path,options=brave)

# driver.get(url)
# driver.get("https://orteil.dashnet.org/experiments/cookie/")

driver.get("https://orteil.dashnet.org/experiments/cookie/")
item_names = [
    "Cursor",
    "Grandma",
    "Factory",
    "Mine",
    "Shipment",
    "Alchemy lab",
    "Portal",
    "Time machine",
    "Elder Pledge"
]
items = [None] * len(item_names)
cookie = driver.find_element_by_id("cookie")


def click_cookie(seconds):
    stop_time = time.time_ns() + seconds * 10**9
    count = 0
    while stop_time > time.time_ns():
        count += 1
        cookie.click()  # 216, 238, 248 clicks per second
    print(f'{count / seconds} clicks per second')


def buy_most_expensive_item():
    # See https://www.selenium.dev/exceptions/#stale_element_reference
    # The JavaScript replaces items with a more expensive one when clicked
    # Recreate the list of items to prevent StaleElementReferenceException
    for i in range(len(items)):
        items[i] = driver.find_element_by_id("buy" + item_names[i])
    for i in range(len(items) - 1, -1, -1):
        if items[i].get_attribute("class") == "":
            items[i].click()
            break


run_time = time.time_ns() + 300 * 10**9  # 5 minute run
delay = 5.0  # Initial seconds
while run_time > time.time_ns():
    click_cookie(seconds=delay)
    buy_most_expensive_item()
driver.get_screenshot_as_file("screenshot.png")

