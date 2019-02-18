import unittest
import my_money


class TestAtmCheckBalance(unittest.TestCase):
    def test_check_balance(self):
        self.assertLessEqual(my_money.atm.check_balance(), 10000)

    def test_check_balance_EnterPin(self):
      with self.assertRaisesRegexp(my_money.EnterPin, "Enter pin first!!!"):(my_money.atm.check_balance())


