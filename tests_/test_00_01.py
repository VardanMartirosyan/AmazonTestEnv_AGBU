import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

userNameFieldElement = driver.find_element(By.ID, "ap_email")
userNameFieldElement.clear()
userNameFieldElement.send_keys("Vardan@gmail.com")

continueButtonElement = driver.find_element(By.ID, "continue")
continueButtonElement.click()

passwordFieldElement = driver.find_element(By.ID, "ap_password")
passwordFieldElement.clear()
passwordFieldElement.send_keys("Martirosyan")

time.sleep(6)
signInButtonElement = driver.find_element(By.ID, "signInSubmit")
signInButtonElement.click()
time.sleep(6)

driver.close()


