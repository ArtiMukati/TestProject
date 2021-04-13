import unittest

from test_SeleniumPythonScript import LoginTest

login_tc = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# Create a test suite
test_suite = unittest.TestSuite([login_tc])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)
