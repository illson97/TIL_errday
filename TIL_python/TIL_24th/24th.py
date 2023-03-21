

# 2441

#N = int(input())
#for i in range(N):
    #print(" " * i + "*" * (N-i))



# 2592


#num_list = [int(input()) for _ in range(10)]

#print(sum(num_list)//10)
#print(max(num_list, key=num_list.count))



# 10798

#list1 = []
#for i in range(5):
    #list1.append(input())

#for i in range(max([len(e) for e in list1])):
    #for j in range(5):
        #if i < len(list1[j]):
            #print(list1[j][i], end ="")



# 9455




# 1652


#N = int(input())
#list1 = []

#for i in range(N):
    #list1.append(input())

#horsum = 0
#versum = 0

#for i in range(N):
    #hor = 0
    #ver = 0
    #for j in range(N):
        #if list1[i][j] == '.':
            #hor += 1
        #elif list1[i][j] == 'X':
            #hor = 0
        #if hor == 2:
            #horsum += 1
        #if list1[j][i] == '.':
            #ver += 1
        #elif list1[j][i] == 'X':
            #ver = 0
        #if ver == 2:
            #versum += 1

#print(horsum,versum)