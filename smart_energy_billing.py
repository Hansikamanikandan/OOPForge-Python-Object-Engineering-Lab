class ElectricityBill:
    def __init__(self, units):
        self.units = units

    def bill(self):
        if self.units <= 100:
            return 0
        elif self.units <= 200:
            return (self.units - 100) * 1.5
        elif self.units <= 300:
            return (self.units - 200) * 2.5 + 150
        else:
            return (self.units - 300) * 4 + 400

    def display(self):
        print("Units:", self.units)
        print("Bill:", self.bill())


units = int(input("Enter units consumed: "))
u = ElectricityBill(units)
u.display()
