class User:
    def __init__(self, name, pin, account_number, bank):
        self.name = name
        self.pin = pin
        self.account_number = account_number
        self.bank = bank
        self.balance = 0

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.bank.modify_balance(-amount)
            return True
        else:
            return False

    def deposit(self, amount):
        self.balance += amount
        self.bank.modify_balance(+amount)

    def view_balance(self):
        return self.balance

    def change_pin(self, new_pin):
        self.pin = new_pin

    def generate_pin(self):
        import random
        self.pin = ''.join(str(random.randint(0, 4)) for _ in range(4))
        return self.pin

    def transfer(self, recipient, amount):
        if self.withdraw(amount):
            recipient.deposit(amount)
            return True
        else:
            return False
        
    def view_details(self):
        return f"Name: {self.name}, Account Number: {self.account_number}, Balance: {self.balance}, Bank: {self.bank.name}"

    def mini_statement(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}, Bank: {self.bank.name}"