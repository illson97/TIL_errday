# 10101

#a = int(input())
#b = int(input())
#c = int(input())

#if a == b == c == 60:               
    #print("Equilateral")
#elif a + b + c == 180:              
    #if a == b or b == c or c == a:  
        #print("Isosceles")
    #else:                           
        #print("Scalene")
#else:                               
    #print("Error")



# 2720

#T = int(input())

#for _ in range(T):
    #C = int(input())        
    #C_list = {25: 0, 10: 0, 5: 0, 1: 0}
    
    #while C:
        #for num in [25, 10, 5, 1]:
            #while C >= num:
                #C -= num
                #C_list[num] += 1
                
    #print(C_list[25], C_list[10], C_list[5], C_list[1]) 


# 1453

#N = int(input())
#list = []
#num = 0
#K = input().split()
#for i in range(N):
    #if K[i] not in list:
        #list.append(K[i])
    #else:
        #num += 1
#print(num)



# 10773

#K = int(input())
#list = []
#for i in range(K):
    #num = int(input())
    #if num == 0:
        #list.pop()
    #else:
        #list.append(num)
#print(sum(list))


# 2161

#from collections import deque

#N = int(input())
#queue = deque(range(1, N + 1))

#while len(queue) > 1:
    #print(queue.popleft(), end=" ")
    #queue.append(queue.popleft())

#print(queue[0])




# 9012

#T = int(input())

#for _ in range(T):
    #K = input()
    #list1 = list(K)
    #sum = 0

    #for i in list1:
        #if i == "(":
            #sum += 1
        #elif i == ")":
            #sum -= 1
        #if sum < 0:
            #print("NO")
            #break

    #if sum > 0:
        #print("NO")
    #elif sum == 0:
        #print("YES")