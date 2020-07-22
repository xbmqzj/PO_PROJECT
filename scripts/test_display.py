import os, sys
sys.path.append(os.getcwd())

from appium import webdriver
import pytest
from base.base_driver import init_driver
from page.display_page import DisplayPage


class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.display_page = DisplayPage(self.driver)

    def test_display_input(self):
        # self.driver.find_element_by_xpath("//*[contains(@text, '显示')]").click()
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.driver.find_elements_by_id("android:id/search_src_text").send_keys("hello")
        # self.driver.find_elements_by_class_name("android.widget.ImageButton").click()
        # 点击显示
        # 点击放大镜
        self.display_page.click_search()
        # 输入文字
        self.display_page.input_text("hello")
        # 点击返回
        self.display_page.click_back()
