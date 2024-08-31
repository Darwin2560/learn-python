# and, or, not operators

use = "Admin"
logged_in = True

if use == "Admin" and logged_in:
    print("Access granted")
else:
    print("Access denied")

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
print(id(a))
print(id(b))
print(a is b)  # False, because they are different objects
print(id(a) == id(b))  # False
b = a
print(a is b)  # True, because they are the same object
print(id(a) == id(b))  # True, because they have the same memory address
