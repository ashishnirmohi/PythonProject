import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import HtmlTestRunner

class loginpage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/home/ucreate-73/PycharmProjects/SeleniumTesting/geckodriver')

    def test_incorrectEmailPassword(self):
        pageUrl = "https://uat-ubrew.herokuapp.com"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)
        sleep(3)
        loginbutton = driver.find_element_by_id("login-btn")
        loginbutton.is_displayed()

        loginbutton.click()

        email = driver.find_element_by_id("user_email")
        email.is_displayed()
        email.send_keys("ashishkumar@ucreate.co.in")

        password = driver.find_element_by_id("user_password")
        password.is_displayed()
        password.send_keys("@Test123")

        signIn = driver.find_element_by_id("signin")
        signIn.is_displayed()
        signIn.click()

        sleep(3)
        driver.find_element_by_class_name("close").click()

    def test_invalidEmailPassword(self):
        pageUrl = "https://uat-ubrew.herokuapp.com"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)
        sleep(3)
        driver.find_element_by_id("login-btn").click()
        driver.find_element_by_id("user_email").send_keys("ashishkumar")
        driver.find_element_by_id("user_password").send_keys("@Test")
        driver.find_element_by_id("signin").click()
        sleep(3)
        driver.find_element_by_class_name("close").click()

    def test_correctEmailPassword(self):
        pageUrl = "https://uat-ubrew.herokuapp.com"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)
        sleep(3)
        driver.find_element_by_id("login-btn").click()
        driver.find_element_by_id("user_email").send_keys("kumaryop42@yopmail.com")
        driver.find_element_by_id("user_password").send_keys("@Test1234")
        driver.find_element_by_id("signin").click()
        driver.find_element_by_class_name("close").click()


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
        unittest.main()


