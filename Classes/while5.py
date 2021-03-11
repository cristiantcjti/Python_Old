index = 0
s = "Mind the gap!"
while index < len(s) and s[index] != " ":
    index += 1
print(s[:index])
