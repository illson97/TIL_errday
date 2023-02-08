

# 1225


#import sys
#input = sys.stdin.readline

#A, B = input().split()

#list1 = list(map(int, A))
#list2 = list(map(int, B))

#print(sum(list1) * sum(list2))





# 2438

#N = int(input())

#for i in range(N):
    #i +=1
    #print("*" * i)




# 2739


#n = int(input())

#for i in range(1, 10):

    #print(n, "*", i, "=", n * i)






# 2953


#list1 = []

#for i in range(5):
    #list1.append(sum(map(int, input().split())))

#print(list1.index(max(list1)) + 1, max(list1))






# 2669


#import sys
#input = sys.stdin.readline

#list1 = [[False]*101 for _ in range(101)]
#for _ in range(4):
    #x1,y1,x2,y2 = map(int,input().split())
    #for i in range(x1,x2):
        #for j in range(y1,y2):
            #list1[i][j] = True
#print(sum(sum(list1[i]) for i in range(101)))