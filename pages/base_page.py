from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from locators.main_locators import HomePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.qa-practice.com/'

    main_locator = HomePageLocators()

    def open_site(self):
        self.driver.get(self.url)

    def press_on_ui_elements(self):
        self.element_is_clickable(self.main_locator.SINGLE_UI_ELEMENTS).click()

    def element_is_clickable(self, locator):
        return W(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator):
        return W(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator):
        return W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator):
        return W(self.driver, 10).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator):
        return W(self.driver, 10).until(EC.presence_of_element_located(locator))

    def check_required_field(self, string_locator, error_locator):
        string = self.element_is_clickable(string_locator)
        validation_message = string.get_attribute('validationMessage')
        required_field = string.get_attribute('required')
        string.send_keys(' ')
        string.send_keys(Keys.ENTER)

        error = self.element_is_visible(error_locator).text

        return validation_message, required_field, error
