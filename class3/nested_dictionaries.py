thisdict = {
    "brand":"Honda",
    "model":"test",
    "year":"2023-01-12"
}
dict2 = {
    "brand":"Honda",
    "model":"test",
    "year":"2023-01-12"
}

dict3 = {
    "brand":"Honda",
    "model":"test",
    "year":"2023-01-12"
}

AllDictionary = {
    "child1":thisdict,
    "child2":dict2,
    "child3":dict3

}


print(AllDictionary.keys())

if 'a' in AllDictionary:
    print('a')
elif 'b' in AllDictionary:
    print('b')
elif 'c' in AllDictionary:
    print('c')
else:
    print('not found')