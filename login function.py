from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\chromedriver_win32 (2)\chromedriver.exe")

#normal function

#valid username and password
driver.get("https://app.vwo.com/#/login")
driver.find_element(By.ID,"login-username").send_keys("#####")
driver.find_element(By.ID,"login-password").send_keys("******")
driver.find_element(By.XPATH,"//div[@class='recaptcha-checkbox-border']").click()
driver.find_element(By.XPATH,"//span[@data-qa='ezazsuguuy']").click()
driver.close()

driver.implicitly_wait(5)

#invalid username and password
driver.get("https://app.vwo.com/#/login")
driver.find_element(By.ID,"login-username").send_keys("#####!!!")
driver.find_element(By.ID,"login-password").send_keys("******************")
driver.find_element(By.XPATH,"//div[@class='recaptcha-checkbox-border']").click()
driver.find_element(By.XPATH,"//span[@data-qa='ezazsuguuy']").click()
driver.close()

driver.implicitly_wait(5)

#valid username invalid password
driver.get("https://app.vwo.com/#/login")
driver.find_element(By.ID,"login-username").send_keys("#####")
driver.find_element(By.ID,"login-password").send_keys("******###")
driver.find_element(By.XPATH,"//div[@class='recaptcha-checkbox-border']").click()
driver.find_element(By.XPATH,"//span[@data-qa='ezazsuguuy']").click()
driver.close()

driver.implicitly_wait(5)

#invalid usernmae and valid password
driver.get("https://app.vwo.com/#/login")
driver.find_element(By.ID,"login-username").send_keys("#####@@@")
driver.find_element(By.ID,"login-password").send_keys("******")
driver.find_element(By.XPATH,"//div[@class='recaptcha-checkbox-border']").click()
driver.find_element(By.XPATH,"//span[@data-qa='ezazsuguuy']").click()
driver.close()

