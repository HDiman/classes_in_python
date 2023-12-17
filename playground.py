# ============= After 5 lesson =============





# ============= After 4 lesson =============








# ---------------------------------------

# Setting pay amount in Developer differ then in Employee
# Python Object-Oriented Programming

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


class Developer(Employee):
    raise_amt = 1.10


dev_1 = Developer("Corey", "Schafer", 50000)
dev_2 = Developer("Jon", "Tracy", 60000)

print(dev_1.pay)
Developer.apply_raise(dev_1)
print(dev_1.pay)


# ============= After 3 lesson =============
# New word - hyphen (дефис)
# Regular, Class and Static methods
# Regular takes Instance as first Argument
# Class methods = @classmethod
# Python Object-Oriented Programming

# Python Object-Oriented Programming

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    # @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Jon", "Tracy", 60000)

import datetime
my_date = datetime.date(2023, 12, 17)

print(Employee.is_workday(my_date))

# ---------------------------------------

# Python Object-Oriented Programming

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    # @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Tracy-90000'

new_emp_2 = Employee.from_str(emp_str_2)
print(new_emp_2.email)

# ---------------------------------------

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


# ---------------------------------------
# Python Object-Oriented Programming

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    # @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Tracy-90000'

new_emp_2 = Employee.from_str(emp_str_2)
print(new_emp_2.email)


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
