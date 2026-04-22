class Student:
    def __init__(self, name, m1, m2, m3, m4, m5, roll_no):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5
        self.roll_no = roll_no

    def total(self):
        return self.m1 + self.m2 + self.m3 + self.m4 + self.m5

    def avg(self, total):
        return total / 5

    def grade(self, avg):
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "Fail"

    def display(self, total, avg, grade):
        print("\n--- Student Report ---")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.m1, self.m2, self.m3, self.m4, self.m5)
        print("Total:", total)
        print("Average:", avg)
        print("Grade:", grade)


name = input("Enter student name: ")
m1 = int(input("Enter mark1: "))
m2 = int(input("Enter mark2: "))
m3 = int(input("Enter mark3: "))
m4 = int(input("Enter mark4: "))
m5 = int(input("Enter mark5: "))
roll_no = int(input("Enter roll no: "))

s = Student(name, m1, m2, m3, m4, m5, roll_no)
t = s.total()
a = s.avg(t)
g = s.grade(a)
s.display(t, a, g)
