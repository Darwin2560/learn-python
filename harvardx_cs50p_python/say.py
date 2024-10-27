import sys

import cowsay
from sayings import hello

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
    hello(sys.argv[1])
