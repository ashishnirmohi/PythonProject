from selenium import webdriver
import unittest
from time import sleep



class EditBooking(unittest.TestCase):
        def setUp(self):
            self.driver = webdriver.Firefox(executable_path='/home/ucreate-73/PycharmProjects/SeleniumTesting/geckodriver')

        def test_editBooking(self):
            pageUrl = "https://uat-ubrew.herokuapp.com"
            driver = self.driver
            driver.maximize_window()
            driver.get(pageUrl)
            driver.find_element_by_id("login-btn").click()
            driver.find_element_by_id("user_email").send_keys("kumaryop32@yopmail.com")
            driver.find_element_by_id("user_password").send_keys("@Test1234")
            driver.find_element_by_id("signin").click()
            sleep(3)

            manage = driver.find_element_by_xpath("//*[@id=\"navbar_left\"]/ul/li[2]/a")
            manage.is_displayed()
            sleep(2)
            manage.click()

            booking = driver.find_element_by_xpath("//*[@id=\"up_coming_103\"]/h5")
            booking.is_displayed()
            sleep(2)
            booking.click()

            edit = driver.find_element_by_xpath("//*[@id=\"manage_upcoming\"]/div/div/div[2]/span[1]")
            edit.is_displayed()
            sleep(2)
            edit.click()

            continu = driver.find_element_by_xpath("//*[@id=\"manage_upcoming\"]/div/div/div[3]/div[1]/span[2]")
            continu.is_displayed()
            sleep(2)
            continu.click()

            confirm = driver.find_element_by_xpath("//*[@id=\"manage_upcoming\"]/div[1]/div/div[3]/div[2]/span[2]")
            confirm.is_displayed()
            sleep(2)
            confirm.click()


            okay = driver.find_element_by_xpath("//*[@id=\"confirm_edit_booking_modal\"]/div/div/div[2]/div/input")
            okay.is_displayed()
            sleep(2)
            okay.click()

        def test_CancelBooking(self):
            pageUrl = "https://uat-ubrew.herokuapp.com"
            driver = self.driver
            driver.maximize_window()
            driver.get(pageUrl)
            driver.find_element_by_id("login-btn").click()
            driver.find_element_by_id("user_email").send_keys("kumaryop32@yopmail.com")
            driver.find_element_by_id("user_password").send_keys("@Test1234")
            driver.find_element_by_id("signin").click()
            sleep(3)

            manage = driver.find_element_by_xpath("//*[@id=\"navbar_left\"]/ul/li[2]/a")
            manage.is_displayed()
            sleep(2)
            manage.click()

            booking = driver.find_element_by_xpath("//*[@id=\"up_coming_103\"]/h5")
            booking.is_displayed()
            sleep(2)
            booking.click()

            cancelBooking = driver.find_element_by_xpath("//*[@id=\"manage_upcoming\"]/div[1]/div/div[2]/span[2]")
            cancelBooking.is_displayed()
            sleep(2)
            cancelBooking.click()

            nocancel = driver.find_element_by_xpath("//*[@id=\"cancel_booking_popup\"]/div[2]/div/input[1]")
            nocancel.is_displayed()
            sleep(2)
            nocancel.click()

        def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
           unittest.main()




