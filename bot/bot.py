from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.imdb.com/')
driver.find_element(By.XPATH , '//*[@id="imdbHeader"]/div[2]/div[5]/a/div').click()
WebDriverWait(driver,10).until(EC.element_to_be_clickable)
sleep(5)
driver.find_element(By.XPATH , '//*[@id="signin-options"]/div/div[1]/a[1]').click()

email = 'REDACTED'
password = 'REDACTED'

WebDriverWait(driver,10).until(EC.element_to_be_clickable)
driver.find_element(By.NAME , 'email').send_keys(email)
driver.find_element(By.NAME , 'password').send_keys(password)
sleep(8)
driver.find_element(By.ID , 'signInSubmit').click()

series = 'stranger things'
driver.find_element(By.NAME , 'q').send_keys(series)
sleep(4)
driver.find_element(By.XPATH , '//*[@id="react-autowhatever-1--item-1"]/a').click()
WebDriverWait(driver,10).until(EC.element_to_be_clickable)
driver.find_element(By.XPATH , '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[2]/button').click()
sleep(3)
WebDriverWait(driver,10).until(EC.visibility_of_element_located)
driver.find_element(By.XPATH , '/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/button[10]').click()
sleep(1)
driver.find_element(By.XPATH , '/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div[2]/button').click()