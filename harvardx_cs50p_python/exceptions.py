def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("Enter the value of x: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            return x


main()
