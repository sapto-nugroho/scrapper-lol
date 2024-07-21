from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# link = "https://lolalytics.com/"
link = "https://lolalytics.com/lol/tierlist/"
driver.get(link)

# btn1 = driver.find_element(By.LINK_TEXT,'LoL Tier List')
# btn1.click()

nama = driver.find_element(By.XPATH,'/html/body/main/div[6]/div[3]')
print(nama.text)

time.sleep(20)
driver.quit()


# /html/body/main/div[6]/div[4]