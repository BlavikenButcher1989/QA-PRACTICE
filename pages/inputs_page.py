import time

from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage

from locators.inputs_locators import InputsPageLocators



class TextInput(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locator = InputsPageLocators()

    def check_text_input_is_required_field(self):
        self.press_on_ui_elements()
        self.element_is_clickable(self.locator.INPUTS).click()
        validation_message, required_field, error = self.check_required_field(
            self.locator.TEXT_STRING,
            self.locator.TEXT_ERROR
        )

        return validation_message, required_field, error

    def check_enter_text_into_field_valid(self, string):
        self.press_on_ui_elements()
        self.element_is_clickable(self.locator.INPUTS).click()
        text_string = self.element_is_clickable(self.locator.TEXT_STRING)
        text_string.send_keys(string)
        text_string.send_keys(Keys.ENTER)
        text_result = self.element_is_visible(self.locator.TEXT_RESULT).text

        return text_result

    def check_enter_text_into_field_invalid(self, string):
        self.press_on_ui_elements()
        self.element_is_clickable(self.locator.INPUTS).click()
        text_string = self.element_is_clickable(self.locator.TEXT_STRING)
        text_string.send_keys(string)
        text_string.send_keys(Keys.ENTER)
        error_text = self.element_is_visible(self.locator.TEXT_ERROR).text

        return error_text

class EmailField(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locator = InputsPageLocators()

    def check_email_field_is_required_field(self):
        self.press_on_ui_elements()
        self.element_is_clickable(self.locator.INPUTS).click()
        self.element_is_clickable(self.locator.EMAIL_FIELD).click()
        validation_message, required_field, error = self.check_required_field(
            self.locator.EMAIL_STRING,
            self.locator.EMAIL_ERROR
        )

        return validation_message, required_field, error

    def check_enter_email_into_field_valid(self, string):
        self.press_on_ui_elements()
        self.element_is_clickable(self.locator.INPUTS).click()
        self.element_is_clickable(self.locator.EMAIL_FIELD).click()
        email_string = self.element_is_clickable(self.locator.EMAIL_STRING)
        email_string.send_keys(string)
        email_string.send_keys(Keys.ENTER)
        email_text_result = self.element_is_visible(self.locator.EMAIL_RESULT_TEXT).text

        return email_text_result

    def check_enter_email_into_field_invalid(self, string):
        self.press_on_ui_elements()
        self.element_is_clickable(self.locator.INPUTS).click()
        self.element_is_clickable(self.locator.EMAIL_FIELD).click()
        email_string = self.element_is_clickable(self.locator.EMAIL_STRING)
        email_string.send_keys(string)
        email_string.send_keys(Keys.ENTER)
        error_text = self.element_is_visible(self.locator.EMAIL_ERROR).text

        return error_text

class PasswordField(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locator = InputsPageLocators()

    def check_password_field_is_required_field(self):
        self.press_on_ui_elements()
        self.element_is_clickable(self.locator.INPUTS).click()
        self.element_is_clickable(self.locator.PASS_FIELD).click()
        validation_message, required_field, error = self.check_required_field(
            self.locator.PASS_STRING,
            self.locator.PASS_ERROR
        )

        return validation_message, required_field, error

    def check_enter_password_into_field_valid(self, string):
        self.press_on_ui_elements()
        self.element_is_clickable(self.locator.INPUTS).click()
        self.element_is_clickable(self.locator.PASS_FIELD).click()
        email_string = self.element_is_clickable(self.locator.PASS_STRING)
        email_string.send_keys(string)
        email_string.send_keys(Keys.ENTER)
        email_text_result = self.element_is_visible(self.locator.PASS_RESULT_TEXT).text

        return email_text_result

    def check_enter_password_into_field_invalid(self, string):
        self.press_on_ui_elements()
        self.element_is_clickable(self.locator.INPUTS).click()
        self.element_is_clickable(self.locator.PASS_FIELD).click()
        email_string = self.element_is_clickable(self.locator.PASS_STRING)
        email_string.send_keys(string)
        email_string.send_keys(Keys.ENTER)
        error_text = self.element_is_visible(self.locator.PASS_ERROR).text

        return error_text