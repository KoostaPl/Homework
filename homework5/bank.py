import json
from datetime import datetime


class InsufficientFunds(Exception):
    pass

class AccountNotFound(Exception):
    pass

class CurrencyMismatch(Exception):
    pass

class Account:
    def __init__(self, currency):
        self.currency = currency
        self.balance = 0.0
        self.transaction_history = []


    def deposit(self, amount):
        if  amount <= 0 :
            raise ValueError("Сумма должна быть положительной.")
        self.balance += amount
        print(f"Счет в {self.currency} пополнен на {amount} {self.currency}. Текущий баланс: {self.balance} {self.currency}")
        print("************************************************")
        self.transaction_history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Пополнение\переводы: +{amount} {self.currency}, текущий баланс {self.balance} {self.currency}")

    def withdraw(self, amount):
        if 0 >= amount:
            raise ValueError("Сумма должна быть положительной.")
        if amount > self.balance:
            raise InsufficientFunds("На счёте недостаточно средств.")
        self.balance -= amount
        print("************************************************")
        print(f"Со счета в {self.currency} снято {amount} {self.currency}. Текущий баланс: {self.balance} {self.currency}")
        print("************************************************")
        self.transaction_history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Снятие\переводы: -{amount} {self.currency}, текущий баланс {self.balance} {self.currency}")

    def get_transaction_history(self):
        return self.transaction_history
    
    def to_dict(self):
        return {
            'currency': self.currency,
            'balance': self.balance,
            'transaction_history': self.transaction_history
        }
    
    @staticmethod
    def from_dict(data):
        account = Account(data['currency'])
        account.balance = data['balance']
        account.transaction_history = data['transaction_history']
        return account

class Client:
    def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name
        self.accounts = {}
        
    def open_account(self, currency):
        if currency in self.accounts:
            raise ValueError("Счёт в этой валюте уже существует.")
        self.accounts[currency] = Account(currency)
        print(f"Открыт счет в валюте {currency} для клиента {self.name}")
        print("************************************************")

    def close_account(self, currency):
        if currency not in self.accounts:
            raise AccountNotFound("Счёт в этой валюте не был найден.\n")
        del self.accounts[currency]
        print(f"Счет в валюте {currency} закрыт для клиента {self.name}")
        print("************************************************")

    def get_account(self, currency):
        if currency not in self.accounts:
            raise AccountNotFound("Счёт в этой валюте не был найден.")
        return self.accounts[currency]
    
    def generate_statement(self):
        statement = f"Выписка по счетам клиента {self.name} (ID: {self.client_id}):\n"
        total_balance = 0.0
        for currency, account in self.accounts.items():
            statement += f"Валюта: {currency}, Баланс: {account.balance}\n"
            total_balance += account.balance
        statement += f"Общий баланс: {total_balance}\n"

        file_name = f"{self.client_id}_statement.txt"
        with open(file_name, "w", encoding='utf-8') as file:
            file.write(statement)
        print(f"Выписка сохранена в {file_name}")

    def get_transaction_history(self):
        history = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} История операций для клиента {self.name} (ID: {self.client_id}):\n"
        for currency, account in self.accounts.items():
            print("*********************************************")
            history += f"\nСчёт в валюте {currency}:\n"
            print("*********************************************")
            for transaction in account.get_transaction_history():
                history += f"  - {transaction}\n"
        return history
    
    def to_dict(self):
        return {
            'client_id': self.client_id,
            'name': self.name,
            'accounts': {currency: account.to_dict() for currency, account in self.accounts.items()}
        }

    @staticmethod
    def from_dict(data):
        client = Client(data['client_id'], data['name'])
        client.accounts = {currency: Account.from_dict(acc_data) for currency, acc_data in data['accounts'].items()}
        return client
    
class Bank:
    def __init__(self, clients=None):
        self.clients = clients if clients is not None else {}

    def add_client(self, client_id, name):
        if client_id in self.clients:
            raise ValueError("Клиент с таким ID уже существует")
        self.clients[client_id] = Client(client_id, name)
        print("\n************************************************")
        print(f"Добавлен клиент {name} с ID {client_id}")
        print("************************************************")

    def get_client(self, client_id):
        if client_id not in self.clients:
            raise ValueError("Клиент не найден")
        return self.clients[client_id]
    
    def transfer(self, from_client_id, from_currency, to_client_id, to_currency, amount):
        from_client = self.get_client(from_client_id)
        to_client = self.get_client(to_client_id)

        from_account = from_client.get_account(from_currency)
        to_account = to_client.get_account(to_currency)

        if from_account.currency != to_account.currency:
            raise CurrencyMismatch("Переводы между разными валютами запрещены.\n************************************************")

        from_account.withdraw(amount)
        to_account.deposit(amount)
        print("\n****************************************************************************")
        print(f"Переведено {amount} {from_currency} из счета клиента {from_client.name} в {from_currency} в счет клиента {to_client.name} в {to_currency}")
        print("\n****************************************************************************")

    def save_state(self, filename='bank_state.json'):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)

    @staticmethod
    def load_state(filename='bank_state.json'):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                clients = {client_id: Client.from_dict(client_data) for client_id, client_data in data['clients'].items()}
                return Bank(clients)
        except FileNotFoundError:
            return Bank()

    def to_dict(self):
        return {
            'clients': {client_id: client.to_dict() for client_id, client in self.clients.items()}
        }

def main():
    bank = Bank.load_state()
    print("*********************************************")
    print("    Добро пожаловать в банковскую систему!   ")
    print("*********************************************")

    while True:
        print("\n1. Добавить клиента.")
        print("2. Войти в систему.")
        print("3. Выйти из системы.")
        print("*********************************************")
        choice = input("Выберите опцию (1-3): ")
        

        if choice == '1':
            client_id = input("Введите ID клиента: ")
            name = input("Введите имя клиента: ")
            try:
                bank.add_client(client_id, name)
                print("Клиент успешно зарегистрирован")
            except ValueError as e:
                print(e)

        elif choice == "2":
            print("************************************************")
            client_id = input("Введите ваш ID: ")
            print("************************************************")
            try:
                client = bank.get_client(client_id)
                print("Вы успешно авторизовались!")
            except ValueError as e:
                print(e)
                continue

            while True:
                print(f"\nДобро пожаловать, {client.name}")
                print("1. Открыть счет.")
                print("2. Закрыть счет.")
                print("3. Пополнить счет.")
                print("4. Снять сумму со счета.")
                print("5. Перевести деньги между счетами.")
                print("6. Сделать выписку по всем счетам.")
                print("7. Посмотреть историю операций.")
                print("8. Выйти из системы")
                print("************************************************")
                action = input("Выберите опцию (1-8): ")

                if action == "1":
                    print("************************************************")
                    currency = input("Введите валюту счёта: ")
                    print("************************************************")
                    try:
                        client.open_account(currency)
                    except ValueError as e:
                        print(e)

                elif action == "2":
                    print("************************************************")
                    currency = input("Введите валюту счёта: ")
                    print("************************************************")
                    try:
                        client.close_account(currency)
                    except AccountNotFound as e:
                        print(e)

                elif action == "3":
                    print("************************************************")
                    currency = input("Введите валюту счета: ")
                    print("************************************************")
                    amount = float(input("Введите сумму для пополнения счёта: "))
                    print("************************************************")
                    try:
                        account = client.get_account(currency)
                        account.deposit(amount)
                    except (AccountNotFound, ValueError) as e:
                        print(e)

                elif action == "4":
                    print("************************************************")
                    currency = input("Введите валюту счета: ")
                    print("************************************************")
                    amount = float(input("Введите сумму для снятия со счёта: "))
                    try:
                        account = client.get_account(currency)
                        account.withdraw(amount)
                    except (AccountNotFound, InsufficientFunds, ValueError) as e:
                        print(e) 

                elif action == '5':
                    print("************************************************")
                    from_currency = input("Введите валюту счета, с которого переводите: ")
                    to_client_id = input("Введите ID клиента, на который переводите: ")
                    to_currency = input("Введите валюту счета, на который переводите: ")
                    amount = float(input("Введите сумму для перевода: "))
                    print("************************************************")
                    try:
                        bank.transfer(client_id, from_currency, to_client_id, to_currency, amount)
                    except (ValueError, AccountNotFound, CurrencyMismatch, InsufficientFunds) as e:
                        print(e) 


                elif action == "6":
                    try:
                        client.generate_statement()
                    except Exception as e:
                        print(f"Ошибка при создании выписки: {e}")

                elif action == "7":
                    print(client.get_transaction_history())

                elif action == "8":
                    break

                else: 
                    print("************************************************")
                    print("Неверный выбор, попробуйте снова")
                    print("************************************************")
              
        
        elif choice == "3":
            bank.save_state()
            print("************************************************")
            print("Вы успешно вышли из программы. Хорошего дня!.")
            print("************************************************")
            break

        else:
            print("************************************************")
            print("Неверный выбор, попробуйте снова")
            print("************************************************")

if __name__ == "__main__":
    main()