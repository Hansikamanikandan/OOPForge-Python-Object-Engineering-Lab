class Employee:
    def __init__(self, name, age, design, basic_pay):
        self.name = name
        self.age = age
        self.design = design
        self.basic_pay = basic_pay

    def salary(self):
        da = 0.10 * self.basic_pay
        hra = 0.20 * self.basic_pay
        gross = self.basic_pay + da + hra
        return gross

    def display(self):
        print("\n--- Employee Details ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Designation:", self.design)
        print("Basic Pay:", self.basic_pay)
        print("Salary:", self.salary())


name = input("Enter your name: ")
age = int(input("Enter your age: "))
design = input("Enter your designation: ")
basic_pay = int(input("Enter your basic pay: "))

e = Employee(name, age, design, basic_pay)
e.display()
