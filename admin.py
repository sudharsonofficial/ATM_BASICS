class Admin:
    def __init__(self, name):
        self.name = name

    def view_bank_details(self, bank):
        return f"Bank: {bank.name}, Balance: {bank.balance}"

    def view_customer_details(self, customer):
        return f"Name: {customer.name}, Account Number: {customer.account_number}, Balance: {customer.balance}"