from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


# ----------------------------- PREPARE OPTIONS  ----------------------------- #
URL = "https://orteil.dashnet.org/experiments/cookie"
TIMEOUT = time.time() + 5
FIVE_MIN = time.time() + 60*5 #5 minutes

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# ----------------------------- GETTING THE URL  ----------------------------- #
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
driver.maximize_window()
driver.get(URL)

# ----------------------------- Game Automation ----------------------------- #
cookie = driver.find_element(By.ID, "cookie")
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_ids = [item.get_attribute("id") for item in items]
print(items_ids)


while True:
    cookie.click()

    if time.time() > TIMEOUT:
        prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        items_prices = []

        for price in prices:
            text = price.text
            if text != "":
                cost = int(text.split("-")[1].strip().replace(",", ""))
                items_prices.append(cost)

        shop_dictionary = {}
        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))

        for n in range(len(items_prices)):
            shop_dictionary[items_ids[n]] = items_prices[n]

        possible_upgrades = {}
        for key, value in shop_dictionary.items():
            if value < money:
                possible_upgrades[key] = value

        maximum_upgrade = max(possible_upgrades, key=possible_upgrades.get)
        driver.find_element(By.ID, maximum_upgrade).click()

        TIMEOUT = time.time() + 5


    # After 5 minutes stop the bot and check cookies per s
    if time.time() > FIVE_MIN:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break



