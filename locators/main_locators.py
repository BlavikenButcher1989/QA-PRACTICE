from selenium.webdriver.common.by import By

class HomePageLocators:

    HOMEPAGE = (By.CSS_SELECTOR, 'a[href="/"]')
    SINGLE_UI_ELEMENTS = (By.CSS_SELECTOR, 'a[href="javascript:;"]')