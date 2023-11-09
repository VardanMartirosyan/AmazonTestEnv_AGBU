from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.loginPage import LoginPage
from pages_.navigationBar import NavigationBar
from pages_.cartPage import CartPage

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.delete_cookie()
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

loginPageObj = LoginPage(driver)
if loginPageObj._get_title() != "Amazon sign-In":
    print("Error: Wrong Page Title")
    exit(3)

loginPageObj.fill_username_field("test_armenia_99@mail.ru")
loginPageObj.validate_continue_button_text()
loginPageObj.click_to_continue_button()
loginPageObj.fill_password_field("anunazganun321")
loginPageObj.click_to_signin_button()

navigationBarObj = NavigationBar(driver)
navigationBarObj.click_to_cart_button()

cartPageObj = CartPage(driver)
cartPageObj.delete_firstProduct_from_cart()


driver.close()