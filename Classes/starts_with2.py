def starts_with(long, short):
    if long[0:len(short)] == short:
        return True
    else:
        return False

print(starts_with("apple", "app"))

print(starts_with("manatee", "mango"))
