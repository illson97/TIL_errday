
# 실습 1번
#a = -7

#if a>=0:
    #print(a)

#else:
    #print(-a)



#실습 2번 풀이(1)
#number_list = [1, 2, 3, 4, 5, 6, 7]

#from collections import Counter
#print(sum(Counter(number_list).values()))



#실습 2번 풀이(2)
#number_list = [1, 2, 3, 4, 5, 6, 7]

#sum = 0
#for i in number_list:
    #sum +=1
#print(sum)



# 실습 3번
#number_list = [1, 2, 3, 4, 5, 6, 7]

#sum = 0
#for i in number_list:
    #sum+=i
#print(sum)



# 실습 4번
#number_list = [1, 2, 3, 4, 5, 6, 7]

#sum = 0
#n = 0

#for i in number_list:
    #sum +=i
    #n += 1

#print(sum/n)



# 실습 5번
#number_list = [-1, 2, 3, 4, 5]

#sum = 1
#for i in number_list:
    #sum *=i
#print(sum)



# 실습 6, 7번


import sys

number_list = [10, 4, 6, 7, 3]
n_min = sys.maxsize
n_max = -sys.maxsize -1

for num in number_list:
    if num > n_max:
        n_max = num
    if num < n_min:
        n_min = num

print(f"min: {n_min}, max: {n_max}")