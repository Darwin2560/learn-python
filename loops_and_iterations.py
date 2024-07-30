
list_number = [1, 2, 3, 4, 5]

for number in list_number:
    for latter in 'abc':
        if number == 3:
            print(f'Found {number}! {latter}')
            # break
            continue
        print(number, latter)

for i in range(1, 11):
    print(i)

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1