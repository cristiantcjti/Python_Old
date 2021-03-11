def good_length(password):
    return len(password) >= 8 and len(password) <= 64

print(good_length("2short"))

print(good_length("nice password, yo"))

print(good_length("This is really much too long for a password. I mean, it's really secure, but I don't want to type this much every time I log in, okay?"))
