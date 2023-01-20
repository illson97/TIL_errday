T = int(input())

for i in range(1, T+1):
    A = list(map(int, input().split()))
    sum1 = 0
   
    
    for j in range(0, len(A)):
        if (j + 1) % 2 != 0:
            sum1 += int(A[j]) * 2            
        else:
            sum1 += int(A[j]) 
    
    if sum1 % 10 == 0:
    	print("#" + str(i), '0')
    else:
        print("#" + str(i), int(10 - sum1 %10))
             
        