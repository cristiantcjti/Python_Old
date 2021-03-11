def good_len(password):
    return len(password) > 8 and len(password) < 64

print(good_len("2short"))

print(good_len("nice password, yo"))

print(good_len("This is really much too long for a password. I mean, it's really secure, but I don't want to type this much every time I log in, okay?"))
