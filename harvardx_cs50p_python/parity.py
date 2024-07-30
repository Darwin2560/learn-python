def main():
    x = int(input('What\'s x? '))
    if is_even(x):
        print(f'{x} is even')
    else:
        print(f'{x} is odd')


def is_even(n):
    return n % 2 == 0

main()

""" if x % 2 == 0:
    print(f'{x} is an even number')
else:
    print(f'{x} is an odd number') """
