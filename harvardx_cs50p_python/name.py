import sys

if len(sys.argv) < 2:
    # saldra de mi programa en ese mismo instante.
    sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

for arg in sys.argv[1:-1]:
    print("The argument provided is:", arg)
