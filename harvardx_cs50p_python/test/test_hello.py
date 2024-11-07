from ..hello import hello


def test_hello():
    assert hello() == "Hello, world"


def test_hello_arg():
    assert hello("Dar") == "Hello, Dar"
