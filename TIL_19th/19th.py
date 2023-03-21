

#2576
#import sys
#list1 = []

#for i in range(7):
    #N = int(sys.stdin.readline())
    #if N % 2 == 1:
        #list1.append(N)
#if list1:
    #print(sum(list1))
    #print(min(list1))
#else:
    #print(-1)



# 10822

#T = map(int, input().split(','))

#print(sum(T))


# 2754

#d = {"A+": 4.3, "A0": 4.0, "A-": 3.7,  "B+": 3.3,  
     #"B0": 3.0, "B-": 2.7, "C+": 2.3, "C0": 2.0, "C-": 1.7, 
     #"D+": 1.3, "D0": 1.0, "D-": 0.7, "F": 0.0}
#print(d[input()])



# 5622

#alpabet_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
#word = input()
    
#time = 0
#for i in range(len(word)):
    #for j in range(len(alpabet_list)):
        #if (word[i] in alpabet_list[j]) == True:
            #time += (j + 3)

#print(time)


# 2577
#A = int(input())
#B = int(input())
#C = int(input())

#nums = list(str(A * B * C))

#for i in range(0, 10):
    #print(nums.count(str(i)))



# 7785

#import sys
#input = sys.stdin.readline

#ch_list = dict()
#N = int(input())

#for i in range(N):
    #A, B = map(str, input().split())
    #if B == 'enter':
        #ch_list[A] = 1
    #else:
        #del ch_list[A]
        
#ch_list = sorted(ch_list.keys(), reverse = True)

#for j in ch_list:
    #print(j)