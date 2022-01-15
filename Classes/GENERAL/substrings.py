# Write your code here
def is_substring (substring, string):
    index = 0
    while index < len(string):
        if string[index: index + len(substring)] == substring:
            return True
        index += 1
    return False
# Below are some calls you can use to test it

# This one should return False
print(is_substring('cadabra', 'abracadabra'))

# This one should return True
print(is_substring('cse', 'abracadabra'))
