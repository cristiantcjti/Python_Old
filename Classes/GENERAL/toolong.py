def too_long(s):
    length = len(s)
    if length > 140:
        return True
    else:
        return False

print("This should be False:")
print(too_long("I'm a short string!"))

print("This should be True:")
print(too_long("Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal."))
