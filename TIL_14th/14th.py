

# 홀수만 더하기

# T = int(input())

# for test_case in range(1, T+1):
    # num = list(map(int, input().split()))
    # sum = 0
    # for i in num:
    	# if i%2==1:
        	# sum += i
    # print("#"+str(test_case), str(sum))




# 연월일 달력

# T = int(input())
# month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# for test_case in range(1, T+1):
    # num = str(input())
    # year = num[0:4]
    # month = num[4:6]
    # day = num[6:8]
    
    # result = ' '   
    # if 0< int(month) <13 and 0< int(day) <= month_days[int(month)]:
        # result = year + '/' + month + '/' + day
    # else:
        # result = '-1'
        
    # print("#" + str(test_case) + " " + result)





# 서랍의 비밀번호

# a, b = map(int, input().split())
# answer = a - b + 1
# print(answer)





# 간단한 N의 약수

# T = int(input())

# for i in range(T):
    # if T % (i + 1)  == 0:
        # print(i + 1, end=" ")




# 새로운 불면증 치료법


# T = int(input())

# for test_case in range(1, T+1):
    # N = int(input())
    # nums = [0] * 10
    
    # i = 1
    # while 0 in nums:
        # num = str(N * i)
        # for j in range(len(num)):
            # nums[int(num[j])] += 1
        # i += 1

    # print("#" + str(test_case) + " " + num)        