# Python Object-Oriented Programming

# lege class
class Employee:
    # class attribute. The same for all instances
    species = 'Human'

    def __init__(self, first, last, pay):
        # first, last, pay are instance attributes
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    # instance method. A function inside a class

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        # {} {} are placeholders


# instance of a class
emp_1 = Employee('Jurre', 'Zwaan', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

print(Employee.fullname(emp_1))


# Manual assingment of employee
# emp_1.first = 'Jurre'
# emp_1.last = 'Zwaan'
# emp_1.email = 'Jurre.Zwaan@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 60000

# print(emp_1.email)
# print(emp_2.email)
