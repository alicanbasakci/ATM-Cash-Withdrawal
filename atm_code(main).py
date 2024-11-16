class BankAccount:
    def __init__(self,starting_balance=13750):
        self.balance = starting_balance

    def withdraw(self):
        try:
            amount= float(input("Enter the amount to be withdrawn: "))
            if amount > self.balance:
                raise ValueError("The withdrawal amount is greater than your balance!")

            self.balance -= amount
            print("Your new balance is: ",self.balance)
        except ValueError as e:
            print("Error", e)

account = BankAccount()
account.withdraw()