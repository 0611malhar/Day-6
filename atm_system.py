class atm:
    def __init__(self, initial_amt, transaction1=0, transaction2=0):
        self.initial_amt = initial_amt
        self.transaction1 = transaction1
        self.transaction2 = transaction2

    def withdraw(self, amount):
        if amount <= self.initial_amt:
            self.initial_amt -= amount
            print("Withdrawal Successful")
            print("Remaining Balance:", self.initial_amt)
        else:
            print("Insufficient Balance")

    def deposit(self, amount):
        self.initial_amt += amount
        print("Deposit Successful")
        print("Updated Balance:", self.initial_amt)

    def check_balance(self):
        print("Current Balance:", self.initial_amt)


pin = 2707
initial_amt = 20000
count = 3

obj = atm(initial_amt)

for i in range(3):
    x = int(input("Enter PIN:"))
    if x == pin:
        print("Correct Password!\nEntering system")
        break
    else:
        print("Wrong PIN!!\nTry Again")
        count -= 1

if count == 0:
    print("System locked")
    exit(1)

choice = input("Enter your choice:\n1. Withdraw\n2. Deposit\n3. Check Balance")

while(choice.lower() != "exit"):

    if choice.lower() == "withdraw":
        transaction1 = int(input("Enter withdrawl amount: "))
        obj.withdraw(transaction1)

    elif choice.lower() == "deposit":
        transaction2 = int(input("Enter deposit amount: "))
        obj.deposit(transaction2)

    elif choice.lower() == "check balance":
        obj.check_balance()

    else:
        print("Invalid Choice\nTry again!!!")

    choice = input("Enter your choice:")
