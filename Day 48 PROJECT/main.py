from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.amazon.com/EDUCIRO-Castle-Building-Kit-Collectible/dp/B09DFLXJ4F/ref=sr_1_1_sspa?crid=3W5CUCX3ZURNK&keywords=harry+potter+lego&qid=1673548294&sprefix=harry%2Caps%2C189&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUEsxQUwzUTJRRVZKJmVuY3J5cHRlZElkPUEwNTE1NTk0MUtCUkg5U0UyQVhXOSZlbmNyeXB0ZWRBZElkPUEwODA3NDY5Mzc2M0REWE5ITEJDQyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('disable-blink-features=AutomationControlled')


s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get(URL)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-offscreen")))

price = driver.find_element(By.CLASS_NAME, "a-offscreen")
print(price.text)


driver.close()
driver.quit()