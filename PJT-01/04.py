
with open("data/fruits.txt", 'r') as f:
    text = f.readlines()
    text = list(map(lambda s: s.strip(), text))

#print(text)
text_dic={}

for i in text:
    if i not in text_dic:
        text_dic[i] = 1
    else:
        text_dic[i] +=1

for i in text_dic:
    i = i.replace("n", "") + " "

newdict = text_dic

print(newdict, end=' ')

f = open('04.txt', 'w', encoding='UTF8')

f.write()