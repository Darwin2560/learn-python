# TODO: forma 1
# names = []
#
# for _ in range(3):
#     names.append(input("What's your name? "))
#
# for name in sorted(names):
#     print(f"Hello, {name}!")

# TODO: Register of names in a file.
# name = input("What's your name? ")
#
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# TODO: Read names from a file
names = []

with open("names.txt") as file:
    for line in sorted(file):
        print(f"Hello, {line.rstrip()}")
