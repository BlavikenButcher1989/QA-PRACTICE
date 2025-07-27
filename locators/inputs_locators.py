from selenium.webdriver.common.by import By


class InputsPageLocators:

    INPUTS = (By.CSS_SELECTOR, 'a[href="/elements/input"]')

    # Text input
    TEXT_INPUT = (By.CSS_SELECTOR, 'a[href="/elements/input/simple"]')
    TEXT_STRING = (By.CSS_SELECTOR, 'input[id="id_text_string"]')
    TEXT_RESULT = (By.CSS_SELECTOR, 'p[id="result-text"]')
    TEXT_ERROR = (By.CSS_SELECTOR, 'span[id="error_1_id_text_string"]')

    # Email field
    EMAIL_FIELD = (By.CSS_SELECTOR, 'a[href="/elements/input/email"]')
    EMAIL_STRING = (By.CSS_SELECTOR, 'input[id="id_email"]')
    EMAIL_RESULT_TEXT = (By.CSS_SELECTOR, 'p[id="result-text"]')
    EMAIL_ERROR = (By.CSS_SELECTOR, 'span[id="error_1_id_email"]')

    # Password field
    PASS_FIELD = (By.CSS_SELECTOR, 'a[href="/elements/input/passwd"]')
    PASS_STRING = (By.CSS_SELECTOR, 'input[id="id_password"]')
    PASS_RESULT_TEXT = (By.CSS_SELECTOR, 'p[id="result-text"]')
    PASS_ERROR = (By.CSS_SELECTOR, 'span[id="error_1_id_password"]')