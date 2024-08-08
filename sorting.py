li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li, reverse=True)
print('Sorted list:\t', s_li)
li.sort() # reverse True
print('Original list:\t', li)

print('********************************')

tup = (9, 1, 8, 2, 7, 3, 6)
s_tup = sorted(tup)
print('Sorted tuple:\t', s_tup)

print('********************************')

d = {'d': 10, 'b': 2, 'a': 5, 'c': 3}
s_d = sorted(d)
print('Sorted dictionary:\t', s_d)

print('********************************')

li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)
print('Sorted list:\t', s_li)

print('********************************')

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return f'Employee({self.name}, {self.age}, {self.salary})'
    
from operator import attrgetter

e1 = Employee('John', 30, 50000)
e2 = Employee('Alice', 25, 45000)
e3 = Employee('Bob', 35, 60000)

employees = [e1, e2, e3]

def e_sort(e):
    return e.name

# s_employees = sorted(employees, key=lambda employee: employee.name)
s_employees = sorted(employees, key=attrgetter('name'))
print(s_employees)
