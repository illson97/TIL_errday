

# 9498

#n = int(input())
#if 90<= n <= 100:
    #print("A")
#elif 80<= n:
    #print("B")
#elif 70<= n:
    #print("C")
#elif 60<= n:
    #print("D")
#else:
    #print("F")



# 9093


#import sys
#T = int(sys.stdin.readline())

#for _ in range(T):
    #org_word = sys.stdin.readline().rstrip().split()

    #for rev_word in org_word:
        #print(rev_word[::-1], end=' ')
    #print()



#11721

#W = input()

#for i in range(0,len(W),10):
    #print(W[i:i+10])





# 2947

#W = list(map(int, input().split()))
#ans = [1, 2, 3, 4, 5]
#while W != ans:
    #for j in range(4):
        #if W[j] > W[j+1]:
            #arr = W[j]
            #W[j] = W[j+1]
            #W[j+1] = arr
            #print(*W)