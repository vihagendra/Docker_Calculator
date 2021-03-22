import unittest

from Calculator import Calculator

from CsvReader import CsvReader

test_data = CsvReader('/src/unittest-all.csv').data


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        for row in test_data:
            self.assertEqual(self.calculator.add(int(row['avalue1']), int(row['avalue2'])), int(row['aresult']))
            self.assertEqual(self.calculator.result, int(row['aresult']))

    def test_subtract_method_calculator(self):
        for row in test_data:
            self.assertEqual(self.calculator.subtract(int(row['svalue1']), int(row['svalue2'])), int(row['sresult']))
            self.assertEqual(self.calculator.result, int(row['sresult']))

    def test_multiply_method_calculator(self):
        for row in test_data:
            self.assertEqual(self.calculator.multiply(int(row['mvalue1']), int(row['mvalue2'])), int(row['mresult']))
            self.assertEqual(self.calculator.result, int(row['mresult']))

    def test_divide_method_calculator(self):
        for row in test_data:
            self.assertEqual(self.calculator.divide(float(row['dvalue1']), float(row['dvalue2'])), float(row['dresult']))
            self.assertEqual(self.calculator.result, float(row['dresult']))



if __name__ == '__main__':
    unittest.main()
