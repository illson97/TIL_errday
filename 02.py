

count = 0

with open('./data/fruits.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        count += 1

with open('./02.txt', 'w') as f:
    f.write(str(count))