import unittest

from homework5.bank import (Account, AccountNotFound, Bank, Client,
                            CurrencyMismatch, InsufficientFunds)


class TestClient(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()
        self.bank.add_client("1", "John")
        self.bank.add_client("2", "Cena")

    def test_open_account(self):
        self.client.open_account("USD")
        self.assertIn("USD", self.client.accounts)
        self.client1.open_account("USD")
        self.assertIn("USD", self.client1.accounts)

    def test_close_account(self):
        self.client.open_account("USD")
        self.client.close_account("USD")
        self.assertNotIn("USD", self.client.accounts)

    def test_get_account(self):
        self.client.open_account("USD")
        account = self.client.get_account("USD")
        self.assertIsInstance(account, Account)

    def test_deposit(self):
        self.client.open_account("USD")
        account = self.client.get_account("USD")
        account.deposit(100.0)
        self.assertEqual(account.balance, 100.0)

    def test_withdraw(self):
        self.client.open_account("USD")
        account = self.client.get_account("USD")
        account.deposit(100.0)
        account.withdraw(50.0)
        self.assertEqual(account.balance, 50.0)

    def test_transfer(self):
        client1 = self.bank.get_client("1")
        client2 = self.bank.get_client("2")

        client1.open_account("USD")
        client2.open_account("USD")

        usd_account1 = client1.get_account("USD")
        usd_account2 = client2.get_account("USD")

        usd_account1.deposit(100.0)

        self.bank.transfer("1", "USD", "2", "USD", 50.0)

        self.assertEqual(usd_account1.balance, 50.0)
        self.assertEqual(usd_account2.balance, 50.0)


if __name__ == "__main__":
    unittest.main()
