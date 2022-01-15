def start_K(word):
  if word[0] == "K":
    return True
  else:
    return False

name = input("Write eitheir Kelly or Abe:")
print(start_K(name))
