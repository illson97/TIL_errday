

# 10039

#sum = 0

#for i in range(5):
    #num = int(input())
    #if num < 40:
        #sum += 40
    #else:
        #sum += num
#print(int(sum / 5))




# 10871
#N, X = map(int, input().split())
#num = list(map(int, input().split()))

#for i in range(N):
    #if num[i] < X: 
        #print(num[i], end = " ")




# 2480

# A, B, C = map(int, input().split())

#if A == B == C:
    #print(10000 + (1000*A))
    
#elif A == B or B == C:
    #print(1000 + (B*100))
    
#elif A == C:
    #print(1000 + (A*100))

#else:
    #print(max(A, B, C)*100)





# 10886

#N = int(input())
#cute = 0
#nocute = 0

#for i in range(0,N):
    #num = int(input())
    #if num == 0:
        #nocute += 1
    #else:
        #cute += 1

#if nocute > cute:
    #print("Junhee is not cute!")

#else:
    #print("Junhee is cute!")



# 2506

#N = int(input())
#K= list(map(int, input().split()))
#sum1 = 0
#sum2 = 0

#for i in range(N):
    #if K[i] == 1:
        #sum1 += 1
        #sum2 += sum1
    #else:
        #sum1 = 0
        
#print(sum2)


