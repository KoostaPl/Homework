import unittest
from homework5.bank import Bank

class TestBankIntegration(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

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
