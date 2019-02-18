import unittest
import my_money


class TestAtmRiseMoney(unittest.TestCase):
    def test_rise_money_Equal(self):
        self.assertEqual(my_money.atm.rise_money(100), 10100)

    def test_rise_money_NotEqual_1(self):
        self.assertNotEqual(my_money.atm.rise_money(0), 10100)

    def test_rise_money_NotEqual_2(self):
        self.assertNotEqual(my_money.atm.rise_money(100), 10000)

    def test_rise_money_NotEqual_3(self):
        self.assertNotEqual(my_money.atm.rise_money(100), 0)

    def test_rise_money_String(self):
        self.assertEqual(my_money.atm.rise_money('100'), 10100)

    def  test_rise_money_Letter(self):
        self.assertEqual(my_money.atm.rise_money(('one hundred'), 10100))





