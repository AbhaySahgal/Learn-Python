#OOP Concepts — Encapsulation & Inheritance (Very Important)

#Encapsulation -> Hiding internal data and controlling access

#Binding data + behavior tohgether and restricting uncontrolled access.

#Inhertance - code reuse + logical Hierarchy


#Task-1
#Secure Bank System


class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance   # private variable

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
            return
        self.__balance += amount
        print(f"{amount} deposited. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdraw amount")
            return
        if amount > self.__balance:
            print("Insufficient balance")
            return
        self.__balance -= amount
        print(f"{amount} withdrawn. Remaining balance: {self.__balance}")

    def transfer(self, other_account, amount):
        if amount <= 0:
            print("Invalid transfer amount")
            return
        if amount > self.__balance:
            print("Transfer failed: insufficient balance")
            return

        self.__balance -= amount
        other_account.__balance += amount
        print(f"{amount} transferred from {self.name} to {other_account.name}")

    def show_balance(self):
        print(f"{self.name} Balance:", self.__balance)


# Creating accounts
a1 = BankAccount("Abhay", 1000)
a2 = BankAccount("Rahul", 500)

a1.deposit(200)
a1.withdraw(300)
a1.transfer(a2, 400)

a1.show_balance()
a2.show_balance()