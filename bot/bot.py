from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.imdb.com/')
driver.find_element(By.XPATH , '//*[@id="imdbHeader"]/div[2]/div[5]/a/div').click()
sleep(5)
driver.find_element(By.XPATH , '//*[@id="signin-options"]/div/div[1]/a[1]').click()

email = 'REDACTED'
password = 'REDACTED'

WebDriverWait(driver,10).until(EC.element_to_be_clickable)
driver.find_element(By.NAME , 'email').send_keys(email)
driver.find_element(By.NAME , 'password').send_keys(password)
sleep(2)
driver.find_element(By.ID , 'signInSubmit').click()