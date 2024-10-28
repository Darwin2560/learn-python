import random

cards = ["jack", "queen", "king"]


def main():
    random.seed(1)
    print(random.choices(cards, k=2))
    print(random.choices(cards, weights=[75, 5, 20], k=2))


if __name__ == "__main__":
    main()
