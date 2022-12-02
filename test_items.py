import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Test_page():
    def test_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        
        button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
        

        assert len(button) > 0, '!!!КНОПКА ПОКУПКИ НЕ НАЙДЕНА!!!'       







