import unittest
import json

class AdditionTest(unittest.TestCase):
    def test_addition(self):
        # Test addition operation
        result = 2 + 2
        expected = 4
        self.assertEqual(result, expected)

if __name__ == '__main__':
    # Run the tests and save the results to a JSON file
    test_results = unittest.main(
        module=None,
        argv=[''],
        exit=False,
        testRunner=unittest.TextTestRunner(resultclass=unittest.TestResult),
    ).result

    # Convert the test results to a JSON format
    json_results = []
    for test_case in test_results.errors + test_results.failures:
        test_name = test_case[0]._testMethodName
        error_message = str(test_case[1])
        json_results.append({"test_name": test_name, "error_message": error_message})

    with open('results.json', 'w') as file:
        json.dump(json_results, file)