import unittest

from Calculator import Calculator

from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data = CsvReader('/src/unittest-addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(int(row['avalue1']), int(row['avalue2'])), int(row['aresult']))
            self.assertEqual(self.calculator.result, int(row['aresult']))





if __name__ == '__main__':
    unittest.main()
