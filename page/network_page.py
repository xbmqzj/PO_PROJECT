from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class NetworkPage(BaseAction):

    more_button = By.XPATH, "//*[contains(@text, '更多')]"
    network_button = By.XPATH, "//*[contains(@text, '移动网络')]"
    first_network_button = By.XPATH, "//*[contains(@text, '首选网络类型')]"
    network_2g_button = By.XPATH, "//*[contains(@text, '2G')]"
    network_3g_button = By.XPATH, "//*[contains(@text, '3G')]"

    def __init__(self, driver):
        # self.driver = driver
        BaseAction.__init__(self,driver)

    def click_more(self):
        # self.driver.find_element_by_xpath("//*[contains(@text, '更多')]").click()
        # self.find_element(self.more_button).click()
        self.click(self.more_button)

    def click_network(self):
        # self.driver.find_element_by_xpath("//*[contains(@text, '移动网络')]").click()
        # self.find_element(self.network_button).click()
        self.click(self.network_button)

    def click_first_network(self):
        # self.driver.find_element_by_xpath("//*[contains(@text, '首选网络类型')]").click()
        # self.find_element(self.first_network_button).click()
        self.click(self.first_network_button)

    def click_2g(self):
        # self.driver.find_element_by_xpath("//*[contains(@text, '2G')]").click()
        # self.find_element(self.network_2g_button).click()
        self.click(self.network_2g_button)

    def click_3g(self):
        # self.driver.find_element_by_xpath("//*[contains(@text, '3G')]").click()
        # self.find_element(self.network_3g_button).click()
        self.click(self.network_3g_button)

    # def find_element(self, loc):
        # return self.driver.find_element(loc[0], loc[1])