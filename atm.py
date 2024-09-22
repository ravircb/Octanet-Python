class ATM:
    def __init__(self, pin):
        self.balance = 0
        self.pin = pin
        self.transaction_history = []

    def check_pin(self, input_pin):
        return input_pin == self.pin

    def balance_inquiry(self):
        return self.balance

    def cash_withdrawal(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        self.transaction_history.append(f"Withdrawal: -${amount}")
        return f"${amount} withdrawn. New balance: ${self.balance}"

    def cash_deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount}")
        return f"${amount} deposited. New balance: ${self.balance}"

    def change_pin(self, old_pin, new_pin):
        if not self.check_pin(old_pin):
            return "Incorrect PIN"
        self.pin = new_pin
        return "PIN changed successfully"

    def view_transaction_history(self):
        return self.transaction_history

def main():
    atm = ATM(pin=1234)

    while True:
        print("\nATM MENU:")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Balance: ${atm.balance_inquiry()}")
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            print(atm.cash_withdrawal(amount))
        elif choice == '3':
            amount = float(input("Enter amount to deposit: "))
            print(atm.cash_deposit(amount))
        elif choice == '4':
            old_pin = int(input("Enter current PIN: "))
            new_pin = int(input("Enter new PIN: "))
            print(atm.change_pin(old_pin, new_pin))
        elif choice == '5':
            history = atm.view_transaction_history()
            if not history:
                print("No transactions yet")
            else:
                for transaction in history:
                    print(transaction)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again")

if __name__ == "__main__":
    main()
