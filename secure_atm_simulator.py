class InvalidPinError(Exception):
    pass


class AccountLockedError(Exception):
    pass


class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance
        self.attempts = 0

    def verify_pin(self, entered_pin):
        if self.attempts >= 3:
            raise AccountLockedError("Account locked due to many attempts")

        if entered_pin != self.pin:
            self.attempts += 1
            raise InvalidPinError("Invalid PIN")

        print("PIN Verified")
        self.attempts = 0
        return True

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawal Successful")
            print("Remaining Balance:", self.balance)


name = input("Enter your name: ")
pin = int(input("Set PIN: "))
balance = int(input("Enter balance: "))

atm = ATM(pin, balance)

while True:
    try:
        entered_pin = int(input("Enter PIN: "))
        if atm.verify_pin(entered_pin):
            choice = input("Withdraw money? (yes/no): ").lower()
            if choice == "yes":
                amount = int(input("Enter amount: "))
                atm.withdraw(amount)
            break
    except Exception as e:
        print(e)
