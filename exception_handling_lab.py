class ExceptionDemo:

    def divide(self):
        try:
            a = int(input("Enter number: "))
            b = int(input("Enter another number: "))
            print("Result:", a / b)
        except ZeroDivisionError:
            print("Cannot divide by zero")

    def access_list(self):
        try:
            lst = [10, 20, 30, 40]
            index = int(input("Enter index: "))
            print("Element:", lst[index])
        except IndexError:
            print("Invalid index")

    def access_dict(self):
        try:
            d = {1: "A", 2: "B"}
            key = int(input("Enter key: "))
            print("Value:", d[key])
        except KeyError:
            print("Invalid key")


obj = ExceptionDemo()
obj.divide()
obj.access_list()
obj.access_dict()
