def digits(number, base=10):
    assert number >= 0
    if number == 0:
        return [0]
    l = []
    while number > 0:
        l.append(number % base)
        number = number // base
        print(l)
    return l


print(digits(1995))