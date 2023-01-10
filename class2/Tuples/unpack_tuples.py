
''' If the number of variables is less than the number of values, 
you can add an * to the variable name and the values will be assigned to the variable as a list:'''

#Example1
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


#Example2
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)