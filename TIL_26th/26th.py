


# 1547

#M = int(input())
#cup = [0, 1, 0, 0]

#for _ in range(M):
    #X, Y = map(int, input().split())
    #cup[X], cup[Y] = cup[Y], cup[X]

#print(cup.index(1))




# 5576

#W = []
#K = []

#for _ in range(10):
    #W.append(int(input()))
#for _ in range(10):
    #K.append(int(input()))

#W.sort()
#K.sort()

#print(sum(W[7:]), sum(K[7:]))




# 2846



#N = int(input())
#Pi = list(map(int, input().split()))
#orm = 0

#for i in range(N):
    #for j in range(i + 1, N):
        #if Pi[j - 1] < Pi[j]:
            #orm = max(orm, Pi[j] - Pi[i])
        #else:
            #break
#print(orm)




# 1251


#alp = input()
#alp_list = []

#for i in range(len(alp) - 2):
    #for j in range(i + 1, len(alp) - 1):
        #for k in range(j + 1, len(alp)):
            #alp_sum = alp[:j][::-1] + alp[j:k][::-1] + alp[k:][::-1]
            #alp_list.append(alp_sum)

#print(min(alp_list))