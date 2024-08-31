print("Imported my_module...")

test = "Test String"


def find_index(to_search, target):
    """Find the index of a value in a sequence."""
    for i, value in enumerate(to_search):
        print(f"Index: {i}, Value: {value}")
        if value == target:
            print(i)
            return i

    return -1
