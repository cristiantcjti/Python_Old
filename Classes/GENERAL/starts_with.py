def starts_with(long, short):
    for pos in range(len(short)):
        if long[pos] != short[pos]:
            return False
    return True

# A call like this should return True:
print(starts_with("apple", "app"))

# And one like this should return False:
print(starts_with("manatee", "mango"))
