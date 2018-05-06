from selenium import webdriver
import unittest
import time
import pytest

@pytest.mark.uitest
class TestFormater(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:5000/ui")
        time.sleep(3)


    def test_compare(self):
        m = self.driver.find_element_by_id("MyMessage")
        print(m.text)
        self.assertEqual(m.text, "WITAJ SWIECIE!")

#    def test_fail(self):
#        m = self.driver.find_element_by_id("MyMessage")
#        self.assertEqual(m.text, "HAKUNA MATATA")

#    def test_link(self):
#        link = self.driver.find_element_by_id("GoogleLink")
#        link.click()

    def test_name(self):
        name = self.driver.find_element_by_id("imie")
        print(name.text)
        self.assertEqual(name.text, "Karola")

    def tearDown(self):
        self.driver.quit()
