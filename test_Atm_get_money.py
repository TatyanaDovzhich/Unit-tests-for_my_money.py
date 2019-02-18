import unittest
import my_money


class TestAtmGetMoney(unittest.TestCase):
    def test_client_can_get_money(self):
        self.assertEqual(my_money.atm.client_can_get_money, False)

    def test_get_money_LessEqual(self):
        self.assertLessEqual(my_money.atm.get_money(100), 10000)

    def test_get_money_AtmBalance(self):
        with self.assertRaisesRegexp(my_money.AtmBalance, "Atm balance is no enough!!!"):(my_money.atm.get_money(10100))

    def test_get_money_EnterPin(self):
        with self.assertRaisesRegexp (my_money.EnterPin, "Enter pin first!!!"): (my_money.atm.get_money(10100))






