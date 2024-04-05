class Bank:
    def __init__(self, name, balance, acc):
        self.name = name
        self.balance = balance
        self.acc = acc
        self.users = []

    def view_balance(self):
        return self.balance
    
    def add_user(self, user):
        self.users.append(user)

    def modify_balance(self, amount):
        self.balance += amount
    
    def gen_acc_no(self):
        self.acc += 1
        return self.acc

    def view_all_customer_details(self):
        if not self.users:
            return "No customers in this bank."
        else:
            details = "Customer Details:\n"
            for user in self.users:
                details += user.view_details() + "\n"
            return details

    def view_details(self):
        return f"Bank: {self.name}, Balance: {self.balance}"