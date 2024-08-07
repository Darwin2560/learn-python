nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each 'n' in nums
""" my_list = []
for n in nums:
    my_list.append(n)
print(my_list) """

""" my_list = [n for n in nums]
print(my_list) """

# I want 'n*n' for each 'n' in nums
""" my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list) """

""" my_list = [n*n for n in nums]
print(my_list) """

# Using  a map + lambda function
""" my_list = map(lambda n: n*n, nums)
print(my_list) """


# ========= a little more difficult =========
# I want 'n' for each 'n' in nums if 'n' is even
""" my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list) """

""" my_list = [n for n in nums if n % 2 == 0]
print(my_list) """

# Using a filter + lambda function
""" my_list = filter(lambda n: n % 2 == 0, nums)
print(list(my_list)) """ # Convert the filter object to a list for printing

# I want a (latter, num) pair for each latter in 'abcd' and each number in '0123'
""" my_list = []
for latter in 'abcd':
    for number in range(4):
        my_list.append((latter, number))
print(my_list) """

""" my_list = [(latter, number) for latter in 'abcd' for number in range(4)]
print(my_list) """ # Print the list directly, no need to convert to a list

# Disctionary Comprehension
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(zip(name, heros)) # This will print a list of tuples

# I want a dict{'name': 'hero'} for each name, hero in zip(names, heros)
""" my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict) """

""" my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict) """ # Print the dictionary directly, no need to convert to a list or a dict comprehension

# set Comprehension
# nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
""" my_set = set()
for num in nums:
    my_set.add(num)
print(my_set)
"""

""" my_set = {num for num in nums}
print(my_set) """

# Generator Expressions
# I wnat to yield 'n*n' for each 'n' in nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

""" def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums) """

my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)
