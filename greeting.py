def greet(name):
    """Return a greeting for the given name.

    Builds 'Hello, ' followed by the name with its first letter
    uppercased, plus an exclamation mark.
    """
    return "Hello, " + name[0].upper() + name[1:] + "!"


if __name__ == "__main__":
    print(greet("world"))
