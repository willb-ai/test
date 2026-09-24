import sys


def greet(name="World"):
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet(" ".join(sys.argv[1:]) or "World"))
