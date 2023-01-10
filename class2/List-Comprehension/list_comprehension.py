# Before
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = []
for x in fruits:
  print(x)
  if "a" in x:
    newlist.append(x)

print(newlist)

# After
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)