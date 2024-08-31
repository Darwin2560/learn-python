"""
LEGB
Local, Enclosing, Global, Built-in
"""

x = "global x"


def test():
    y = "local y"
    # print(y)
    print(x)


test()
# print(y) # NameError: name 'y' is not defined


def outer():
    x = "outer x"

    def inner():
        x = "inner x"
        print(x)

    inner()
    print(x)


outer()
