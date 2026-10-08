#Lab 1: Introduction to OOP & Classes
#Part 1: Real-World Modeling (Table Class)
class Table:

    def __init__(self, color, material, size):
        self.color = color
        self.material = material
        self.size = size

    def move(self):
        print(f"The {self.color} {self.material} table is being moved to a new location.")

    def describe(self):
        print(f"This is a {self.size}-sized table made of {self.material}.")

#Part 2: State Management & Encapsulation (BankAccount Class)
class BankAccount:
    def __init__(self, holder: str, initial_balance: float = 0.0):
        self.holder = holder
        self.__balance = max(0.0, float(initial_balance))

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount
            print(f"Successfully deposited ${amount}. New Balance: ${self.__balance}")
        else:
            print("Deposit failed: Amount must be greater than zero.")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print("Withdrawal failed: Amount must be greater than zero.")
        elif amount <= self.__balance:
            self.__balance -= amount
            print(f"Successfully withdrew ${amount}. Remaining Balance: ${self.__balance}")
        else:
            print(f"Transaction Declined: Insufficient funds! Requested ${amount}, but available balance is ${self.__balance}.")

    def get_balance(self) -> float:
        """Getter method to safely inspect the private balance."""
        return self.__balance

#TESTING GROUNDS

if __name__ == "__main__":
    print("Part 1: Real-World Modeling")
    
    table1 = Table(color="Brown", material="Oak Wood", size="Large")
    table2 = Table(color="Cristal", material="Tempered Glass", size="Medium")

    print(f"Table 1 Color: {table1.color}")
    print(f"Table 2 Material: {table2.material}")

    table1.describe()
    table1.move()

    table2.describe()
    table2.move()

    print("\n--- PART 2: TESTING BANKACCOUNT CLASS ---")

    account = BankAccount(holder="Aldo Carrillo", initial_balance=500.0)
    print(f"Account Holder: {account.holder}")
    print(f"Initial Balance: ${account.get_balance()}")

    # 2. Perform a deposit and verify updated balance
    print("\nDepositing $250.00...")
    account.deposit(250.0)

    print("\nWithdrawing $100.00...")
    account.withdraw(100.0z

    print("\nAttempting invalid withdrawal of $1000.00...")
    account.withdraw(1000.0)

    print("\nTesting")
    try:
        print(account.__balance)
    except AttributeError as e:
        print(f"Protected {e}")