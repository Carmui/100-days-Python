from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSf3YpfbfgFCA2nu74Px9VheSh0JGcCv-jcl6hC0ypuUQhqWtg/viewform?usp=sf_link"
ZILLOW_LINK = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"

headers = {
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.amazon.com/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

# ---------------------------------- CONFIGURATE CONNECTION  ---------------------------------- #
page = ''
while page == '':
    try:
        response = requests.get(ZILLOW_LINK, headers=headers)
        break
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        time.sleep(5)
        continue


# ---------------------------------- SCRAPPING ZILLOW DATA ---------------------------------- #
data = response.text
soup = BeautifulSoup(data, 'html.parser')


all_links_elements = soup.find_all("a", attrs={'data-test':'property-card-link'})
links = []

for link in all_links_elements:
    href = link["href"]
    if "http" not in href:
        href_fix = f"https://www.zillow.com{href}"
        links.append(href_fix)
    else:
        links.append(href)

all_addresses_elements = soup.find_all("address", attrs={'data-test': 'property-card-addr'})
addresses = [addr.getText().split(" | ")[-1] for addr in all_addresses_elements]

all_prices_elements = soup.find_all("span", attrs={'data-test': 'property-card-price'})
prices = [price.getText().split('+')[0].replace("/mo", "") for price in all_prices_elements]

# ---------------------------------- SELENIUM CONFIG ---------------------------------- #
options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
driver.maximize_window()

# ---------------------------------- USING SELENIUM TO FILL GOOGLE FORM ---------------------------------- #

for n in range(len(addresses)):
    # GETTING FORM URL
    driver.get(FORM_LINK)

    time.sleep(3)
    # XPATH TO ALL FORMS
    address_form = driver.find_element(By.XPATH, '//form[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_form = driver.find_element(By.XPATH, '//form[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_form = driver.find_element(By.XPATH, '//form[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div')

    # SENDING KEYS
    address_form.send_keys(addresses[n])
    price_form.send_keys(prices[n])
    link_form.send_keys(links[n])
    submit_button.click()

