# ============= After 5 lesson =============





# ============= After 4 lesson =============




# ============= After 3 lesson =============
# New word - hyphen (дефис)
# Regular, Class and Static methods
# Regular takes Instance as first Argument
# Class methods = @classmethod
# Python Object-Oriented Programming

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + 'company.com'

        Employee.num_of_emps += 1

    # @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Jon", "Tracy", 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)










# ============= After 2 lessons =============

# Python Object-Oriented Programming

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + 'company.com'

        Employee.num_of_emps += 1

    # @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Jon", "Tracy", 60000)

print(Employee.num_of_emps)