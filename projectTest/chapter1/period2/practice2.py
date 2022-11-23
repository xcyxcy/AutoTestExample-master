import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://localhost:63342/AutoTestExample-master/projectHtml/chapter1/period2/index.html?_ijt=dqv53rvk3rjs5h5pek79i87esq'
edgeDriver = webdriver.Edge()
edgeDriver.get(url)
edgeDriver.maximize_window()
edgeDriver.find_element(By.ID,'email').send_keys('tynam@test.com')
edgeDriver.find_element(By.NAME,'password').send_keys('123')
edgeDriver.find_element(By.ID,'btn-login').click()
time.sleep(3)
edgeDriver.quit()