import unittest
import my_money


class TestAtmEnterPin(unittest.TestCase):
    def test_correct_pin(self):
        self.assertEqual(my_money.atm.enter_pin(777), True)

    def test_incorrect_pin_1(self):
        self.assertNotEqual(my_money.atm.enter_pin(777), 776)

    def test_incorrect_pin_2(self):
        self.assertNotEqual(my_money.atm.enter_pin(777), 778)

    def test_incorrect_pin_3(self):
        self.assertNotEqual(my_money.atm.enter_pin(777), 000)

    def test_attempts(self):
        self.assertEqual(my_money.atm.attempts, 2)

    def test_enter_pin_with_incorrect_pin(self):
        with self.assertRaisesRegexp(my_money.IncorrectPin, "Incorrect Pin!!!"):(my_money.atm.enter_pin(111))

    def test_count_attempts_with_attempts_over(self):
        with self.assertRaises(my_money.AttemptsOver, "Attempts are over!!!"): (my_money.atm.attempts, 0)


