from selenium import webdriver
import unittest
import time
import pytest

@pytest.mark.uitest
class TestFormater(unittest.TestCase):
    def test_plain_lowercase(self):
        driver = webdriver.Chrome()
        driver.get("http://www.google.com")
        driver.find_element_by_id("lst-ib").send_keys("selenium")
        driver.find_element_by_xpath('//input[@value="Szukaj w Google"]').click()
        time.sleep(5)
        driver.quit()
