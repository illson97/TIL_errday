

# 2525


#H, M = map(int, input().split())
#timer = int(input())

#H += timer // 60
#M += timer % 60

#if M >= 60:
    #H += 1
    #M -= 60
#if H >= 24:
    #H -= 24

#print(H, M)






# 2798


#N, M = map(int, input().split())
#card = list(map(int, input().split()))
#sum1 = 0

#for i in range(N - 2):
    #for j in range(i + 1, N - 1):
        #for k in range(j + 1, N):
            #sum_card = card[i] + card[j] + card[k]
            #if sum_card <= M:
                #sum1 = max(sum1, sum_card)

#print(sum1)





# 9076


#T = int(input())

#for i in range(T):
    #N = list(map(int, input().split()))
    #N.pop(N.index(max(N)))
    #N.pop(N.index(min(N)))

    #if max(N) - min(N) >= 4:
        #print("KIN")
    #else:
        #print(sum(N))





# 1436


#N = int(input())
#num = 666

#while N:
    #if '666' in str(num):
        #N -= 1
    
    #num += 1
#print(num - 1)






# 1526


#import sys

#N = int(sys.stdin.readline().rstrip())

#for i in range(N):
    #cnt = 0
    #for j in str(N - i):
        #if j == "7" or j == "4":
            #pass
        #else:
            #cnt = 1
            #break
    #if cnt == 0:
        #break
#print(N - i)