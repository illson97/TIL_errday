


# 10817

#T = map(int, input().split())
#num = sorted(T)
#print(num)



# 20001

#gomu_start = input()
#prob = 0

#while True:
    #gomu = input()

    #if gomu == "고무오리 디버깅 끝":
        #break
    #else:
        #if gomu == "문제":
            #prob += 1
        
        #elif gomu == "고무오리":
            
            #if prob == 0:
                #prob += 2
            #else:
                #prob -= 1

#if prob == 0:
    #print("고무오리야 사랑해") 
#else:
    #print("힝구")




# 1269


#import sys

#A, B = map(int, sys.stdin.readline().split())

#A_list = set(map(int, input().split()))
#B_list = set(map(int, input().split()))

#print(len(A_list ^ B_list))




# 3052


#num = []
#for i in range(10):
    #a = int(input())
    #num.append(a%42)
#print(len(set(num)))




# 1181


#import sys

#N = int(sys.stdin.readline())
#words = []
#for i in range(N):
    #K = sys.stdin.readline().strip()
    #if K not in words:
        #words.append(K)
#words.sort()
#words.sort(key=lambda x:len(x))

#for i in range(len(words)):
    #print(words[i])




# 11286


#import heapq
#import sys

#N = int(sys.stdin.readline())
#list1 = []

#for N in range(N):
    #x = int(sys.stdin.readline())
    #if x !=0:
        #heapq.heappush(list1, (abs(x), x))
    #else:
        #try:
            #print(heapq.heappop(list1)[1])
        #except:
            #print(0)