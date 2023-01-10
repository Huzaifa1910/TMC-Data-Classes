# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

#Error
x = ("apple", "banana", "cherry")
x[1] = "kiwi"
print(x)

#Correct Way
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
print(y)
x = tuple(y)

print(x)