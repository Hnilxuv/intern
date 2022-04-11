class Bank_Account:
    def __init__(self, name, acc_number, balance=0):
        self.name = name
        self.acc_number = acc_number
        self.balance = balance

    def deposit(self):
        amount = int(input("Enter amount to be deposited:"))
        while amount < 0:
            print("Invalid Amount!")
            amount = int(input("Enter amount to be deposited:"))
        else:
            self.balance += amount
            print("Amount deposit:", amount)

    def withdraw(self):
        amount = int(input("Enter amount to be withdraw:"))
        while amount >= self.balance:
            print("Invalid Amount!")
            amount = int(input("Enter amount to be withdraw:"))
        else:
            if amount < 100000:
                amount += 1000
                self.balance -= amount
                print("Amount Withdraw:", amount)
            else:
                amount += amount/100
                self.balance -= amount
                print("Amount Withdraw:", amount)

    def show_details(self):
        print("Bank Account Detail:")
        print("Name:", self.name)
        print("Account Number:", self.acc_number)
        print("Balance:", self.balance)


acc = Bank_Account("Vu Linh", 888888, 100000)
acc.show_details()
acc.deposit()
acc.withdraw()
acc.show_details()
