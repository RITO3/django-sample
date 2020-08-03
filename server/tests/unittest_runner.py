import unittest
import xmlrunner

test_suite = unittest.TestSuite()
all_test_cases = unittest.defaultTestLoader.discover(".", "*.py")
# Loop the found test cases and add them into test suite.
for test_case in all_test_cases:
    test_suite.addTests(test_case)

test_runner = xmlrunner.XMLTestRunner(output="./ci_result/unittest")
test_runner.run(test_suite)
