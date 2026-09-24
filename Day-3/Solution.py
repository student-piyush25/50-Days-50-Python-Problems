# Merge two dictionaries and add values for comman keys.

dict1 = {'a':10, 'b':20, 'c':30}
dict2 = {'b':5, 'c':10, 'd':15}

result = {}

for key in dict1:
    result[key] = dict1[key]
for key in dict2:
    if key in result:
        result[key] = result[key] + dict2[key]
    else:
        result[key] = dict2[key]

print(result)
