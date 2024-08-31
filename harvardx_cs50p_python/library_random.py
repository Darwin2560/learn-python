import random

lits = [
    "a",
    "b",
    "c",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

random_letter = random.choice(lits)
print(random_letter)

print("============================================================")

number = random.randint(1, 100)
print(number)

print("============================================================")

cards = ["jack", "queen", "king", "ace"]
random.shuffle(cards)
for card in cards:
    print(card)
