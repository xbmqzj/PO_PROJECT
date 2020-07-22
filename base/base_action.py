from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        self.driver.find_element(loc).click()

    def find_element(self, loc):
        by = loc[0]
        value = loc[1]
        WebDriverWait(self.driver, 5, 1).until(lambda x:x.find_element(by, value))

    def input_search_text(self, loc, text):
        self.driver.find_element(loc).send_keys(text)

    def find_elements(self, loc):
        by = loc[0]
        value = loc[1]
        WebDriverWait(self.driver, 5, 1).until(lambda x:x.find_elements(by, value))

