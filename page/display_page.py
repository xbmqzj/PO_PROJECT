from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class DisplayPage(BaseAction):

    # 显示按钮
    display_button = By.XPATH, "//*[contains(@text, '显示')]"
    # 搜索按钮
    search_button = By.ID, "com.android.settings:id/search"
    # 搜索框
    input_button = By.ID, "android:id/search_src_text"
    # 返回
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self, driver):
        BaseAction.__init__(driver)
        # self.driver = driver
        # # 点击显示（init里面可以去去屑已经确定的这个模块的所有的前置功能）
        self.click_display()

    def click_display(self):
        # self.driver.find_element_by_xpath("//*[contains(@text, '显示')]").click()
        # self.driver.find_element(*self.display_button).click()
        # self.find_element(self.display_button).click()
        self.click(self.display_button)

    def click_search(self):
        # self.driver.find_element(self.search_button).click()
        # self.find_element(self.search_button).click()
        self.click(self.search_button)

    def input_text(self, text):
        # self.driver.find_element(self.input_button).send_keys(text)
        # self.find_element(self.input_button).send_keys(text)
        self.input_text(self.input_button, text)

    def click_text_view(self):
        # self.driver.find_element(By.ID, "android:id/search_src_text").click()
        self.click(self.input_button)

    def click_back(self):
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        # self.driver.find_element(self.back_button).click()
        # self.find_element(self.back_button).click()
        self.click(self.back_button)

    # def find_element(self, loc):
    #     return self.driver.find_element(loc[0], loc[1])