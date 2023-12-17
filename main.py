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

