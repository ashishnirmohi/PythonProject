import unittest
from HtmlTestRunner import HTMLTestRunner
from ubrew.homepage import launch_homepage
from ubrew.register import registerUbrew
from ubrew.login import loginpage
import os

result_dir = os.getcwd()

loginpage=unittest.TestLoader().loadTestsFromTestCase(loginpage)
launch_homepage = unittest.TestLoader().loadTestsFromTestCase(launch_homepage)
registerUbrew = unittest.TestLoader().loadTestsFromTestCase(registerUbrew)
EditBooking = unittest.TestLoader().loadTestsFromTestCase(EditBooking)
test_suite = unittest.TestSuite([loginpage,launch_homepage,registerUbrew,EditBooking])
#unittest.TextTestRunner(verbosity=2).run(test_suite)
runner = HTMLTestRunner(output='example_suite')
runner.run(test_suite)

#outfile = open(result_dir +"\smoketestreport.html", 'wb')
#runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report',description='Smoke Tests')
#runner.run(test_suite)

