def find_512():
    for x in range(100):
        for y in range(100):
            if x * y == 512:
                 break   # does not do what we want!
    return f"{x} * {y} == 512"
