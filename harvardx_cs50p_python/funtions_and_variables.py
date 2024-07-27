

#TODO: Ask user for their name
name = input('What\'s your name? ').strip().title() # Remove whitespace from string and Capitalize User's name
first, last = name.split(" ")
#TODO: Say hello to user
'''
PARAMETERS
-> end
-> sep
'''

print(f'hello, {first}', end='')
print('.')

# Integer

x = input('What\'s x? ')
y = input('What\'s y? ')
result = int(x) + int(y)
print(f'Sum result: {result}')

# Float
x = input('What\'s x? ')
y = input('What\'s y? ')
result = float(x) + float(y)
result_2 = float(x) / float(y)
# print(round(result_2, 2))
print(f'{result_2:.2f}')
# print(f'Sum result: {round(result):,}')


# Functions
def main():
    # name = input('What\'s your name')
    # hello(name)
    x = int(input('What\'s x? '))
    print(f'x squared is {square(x)}')

def square(n):
    return pow(n, 2)

def hello(to="world"):
    print(f'Hello, {to}')

main()
