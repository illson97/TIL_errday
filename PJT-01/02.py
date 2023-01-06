
result_f = open("data/fruits.txt", 'r')
cnt = 0

while True:
    if result_f.readline() =='':
        break
    cnt +=1
    
print(cnt)

result_f.close()

f = open('02.txt', 'w', encoding='UTF8')

f.write('394')