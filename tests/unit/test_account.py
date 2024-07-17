import unittest
from homework5.bank import Account, InsufficientFunds

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account("USD")

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 0.0)

    def test_deposit(self):
        self.account.deposit(100.0)
        self.assertEqual(self.account.balance, 100.0)

    def test_withdraw_sufficient_funds(self):
        self.account.deposit(100.0)
        self.account.withdraw(50.0)
        self.assertEqual(self.account.balance, 50.0)

    def test_withdraw_insufficient_funds(self):
        self.account.deposit(100.0)
        with self.assertRaises(InsufficientFunds):
            self.account.withdraw(150.0)

if __name__ == "__main__":
    unittest.main()
