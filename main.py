# Python Object-Oriented Programming

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Jon", "Tracy", 60000)

print(emp_1)
print(emp_2)

# emp_1.first = "Corey"
# emp_1.last = "Schafer"
# emp_1.email = 'Corey.Schafer@company.com'
# emp_1.pay = 50000
#
# emp_2.first = "Jon"
# emp_2.last = "Tracy"
# emp_2.email = 'Jon.Tracy@company.com'
# emp_2.pay = 60000

print(emp_1.first)
print(emp_2.first)
