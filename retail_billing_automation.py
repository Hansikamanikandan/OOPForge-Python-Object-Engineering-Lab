class BillingSystem:
    def __init__(self):
        self.items = []
        self.sub_tot = []
        self.total = 0

    def get_items(self, n):
        for _ in range(n):
            name = input("Enter name: ")
            quantity = int(input("Enter quantity: "))
            price = int(input("Enter price: "))
            self.items.append((name, quantity, price))

    def calculate_subtotal(self):
        for item in self.items:
            sub = item[1] * item[2]
            self.sub_tot.append(sub)

    def calculate_total(self):
        self.total = sum(self.sub_tot)

    def apply_discount(self):
        if self.total > 3000:
            discount = self.total * 0.10
            self.total -= discount

    def apply_gst(self):
        gst = self.total * 0.05
        self.total += gst
        print("GST:", gst)

    def display(self):
        print("\nItems:", self.items)
        print("Sub Totals:", self.sub_tot)
        print("Total:", self.total)


n = int(input("Enter number of items: "))
obj = BillingSystem()
obj.get_items(n)
obj.calculate_subtotal()
obj.calculate_total()
obj.apply_discount()
obj.apply_gst()
obj.display()
