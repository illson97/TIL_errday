


# 10769

#mes = input()

#if mes.count(":-)") == 0 and mes.count(":-(") == 0:
    #print("none")
#elif mes.count(":-)") == mes.count(":-("):
    #print("unsure")
#elif mes.count(":-)") > mes.count(":-("):
    #print("happy")
#else:
    #print("sad")




# 2455

#import sys
#input = sys.stdin.readline
#res = 0
#max_res = 0
#for i in range(4):
    #a, b = map(int, input().split())
    #res -= a
    #res += b
    #max_res = max(max_res, res)
#print(max_res)





# 2606

#N = int(input())
#M = int(input())
#graph = [[]*N for i in range(N+1)]
#for i in range(M):
    #A, B = map(int, input().split())
    #graph[A].append(B)
    #graph[B].append(A)
    
#cnt = 0
#visit = [0] * (N+1)

#def dfs(start) : 
    #global cnt
    #visit[start] = 1
    #for i in graph[start] :
        #if visit[i] == 0:
            #dfs(i)
            #cnt += 1
            
#dfs(1)
#print(cnt)