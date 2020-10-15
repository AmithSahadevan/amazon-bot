from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.amazon.in")

try:
    search = WebDriverWait(driver, 1000).until(
        lambda x: x.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
    )
    search.send_keys("realme 6i")
    search.send_keys(Keys.RETURN)

    clicklink = WebDriverWait(driver, 1000).until(
        lambda x: x.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[2]/div[1]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a")
    )
    clicklink.click()
except:
    driver.quit()