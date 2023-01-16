from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
driver.maximize_window()
driver.get(URL)
wait = WebDriverWait(driver, 10)
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
#article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, "Commons")
#all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


#driver.close()
#driver.quit()