

f = open("data/fruits.txt", 'r')

result = []
for value in f:
    if value not in result:
        result.append(value)
        
print(result)


