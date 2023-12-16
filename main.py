# Python Object-Oriented Programming

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + 'company.com'

    # @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Jon", "Tracy", 60000)


print(emp_1.fullname())

print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))

