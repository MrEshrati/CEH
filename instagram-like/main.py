from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

username = 'REDACTED'
password = 'REDACTED'

WebDriverWait(driver,10).until(EC.element_to_be_clickable)
driver.find_element(By.NAME , 'username').send_keys(username)
driver.find_element(By.NAME , 'password').send_keys(password)

driver.find_element(By.XPATH , '//*[@id="loginForm"]/div/div[3]/button').click()
sleep(8)
driver.get('https://www.instagram.com/p/CgPlcpfolUV/')
sleep(3)
emoji = '❤️'

driver.find_element(By.TAG_NAME , '<textarea aria-label="Add a comment…" placeholder="Add a comment…" class="_ablz _aaoc" autocomplete="off" autocorrect="off" style="height: 18px !important;"></textarea>').send_keys(emoji)

