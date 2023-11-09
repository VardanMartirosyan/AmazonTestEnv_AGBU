from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__cartButtonLocator = (By.ID, "nav-cart-count-container")

    def click_to_cart_button(self):
        cardbuttonElement = self._find_element(self.__cartButtonLocator)
        self._click(cardbuttonElement)