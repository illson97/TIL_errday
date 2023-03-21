

# 9085

#T = int(input())

#for i in range(T):
    #num = []
    #N = int(input())
    #num = sum(list(map(int, input().split())))
    #print(num)



# 10824

#A, B, C, D = map(str, input().split())

#print(int(A+B) + int(C+D))





# 3009

#X = []
#Y = []

#for _ in range(3):
    #num1, num2 = map(int, input().split())
    #if num1 in X:
        #X.remove(num1)
    #else:
        #X.append(num1)
    #if num2 in Y:
        #Y.remove(num2)
    #else:
        #Y.append(num2)
        
#print(X[0], Y[0])





# 10952

#while True:
    #a, b = map(int, input().split())
    #if a==0 and b==0:
        #break
    #print(a+b)






# 1110

#n = int(input())
#num = n
#cnt = 0

#while True:
    #a = num//10 
    #b = num%10
    #c = (a+b)%10 
    #num = (b*10)+c
    
    #cnt +=1
    #if (num==n):
        #break
#print(cnt)


