person = {"name": "John Doe", "age": 30, "city": "New York"}

sentence = f"My name is {person['name']}, I am {person['age']}"
print(sentence)

print("================================================================")


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


pi = Person("John Doe", 30, "New York")

sentence = f"My name is {pi.name}, I am {pi.age}"
print(sentence)

print("================================================================")

for i in range(1, 11):
    sentence = f"The value is {i:02}"
    print(sentence)

print("================================================================")

pi = 3.14159265

sentence = f"Pi is equal to {pi:.2f}"
print(sentence)

print("================================================================")

sentence = f"1 MB is equal to {1024 ** 2:,.2f} bytes"
print(sentence)

print("================================================================")

import datetime

my_date = datetime.datetime(2024, 8, 9, 11, 56, 45)
print(my_date)

sentence = f"The date is {my_date:%B %d, %Y}"
print(sentence)

sentence = f"{my_date:%B %d, %Y} fell on a {my_date:%A} and was the {my_date:%j} day of the year"
print(sentence)
