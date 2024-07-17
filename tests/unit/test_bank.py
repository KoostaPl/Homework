import unittest
from homework5.bank import Bank, Client, Account, AccountNotFound, CurrencyMismatch, InsufficientFunds

class TestBank(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

    def test_add_client(self):
        self.bank.add_client("1", "John")
        self.assertIn("1", self.bank.clients)

    def test_get_client(self):
        self.bank.add_client("1", "John")
        client = self.bank.get_client("1")
        self.assertIsInstance(client, Client)
        self.assertEqual(client.name, "John")

    def test_transfer(self):
        self.bank.add_client("1", "John")
        self.bank.add_client("2", "Alice")
        john = self.bank.get_client("1")
        alice = self.bank.get_client("2")
        john.open_account("USD")
        alice.open_account("USD")
        john_account = john.get_account("USD")
        alice_account = alice.get_account("USD")
        john_account.deposit(100.0)
        self.bank.transfer("1", "USD", "2", "USD", 50.0)
        self.assertEqual(john_account.balance, 50.0)
        self.assertEqual(alice_account.balance, 50.0)

if __name__ == "__main__":
    unittest.main()
