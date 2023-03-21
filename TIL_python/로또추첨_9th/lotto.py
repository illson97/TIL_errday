#import random
#lotto = []
#while len(lotto) < 6:
    #num = random.randint(1,45)
    #if num not in lotto:
        #lotto.append(num)

#print(sorted(lotto))



    

#dict_variable = {}
#dict_variable["이름"] = "이정일"
#dict_variable["생년월일"] = "19970223"
#dict_variable["회사"] = "파이썬 풀스택"

#print(dict_variable["이름"])
#print(dict_variable["생년월일"])
#print(dict_variable["회사"])



#dict_variable = {"a": "정일", "b": "바보"}
#dict_variable["c"] = "멍청이"
#dict_variable["D"] = "메롱"
#dict_variable["e"] = "최고"

#print(dict_variable["a"])
#print(dict_variable["D"])
#print(dict_variable["b"])


#dict_variable = {}
#dict_variable["apple"] = 5000
#dict_variable["banana"] = 3000
#dict_variable["apple"] = 2000
#dict_variable["banana"] = dict_variable["banana"] + 1000

#print(dict_variable["apple"] + dict_variable["banana"])


#dict_variable = {"이름": "이정일", "생년월일": "19970223", "회사": "파이썬 풀스택"}

#for key in dict_variable:
    #print(key, dict_variable[key])

"""
예측
이름 이정일
생년월일 19970223
회사 파이썬 풀스택
"""


#dict_variable = {"이름": "이정일", "생년월일": "19970223", "회사": "파이썬 풀스택"}

#print("나이" in dict_variable)



#dict_variable = {"이름": "이정일", "생년월일": "19970223", "회사": "파이썬 풀스택"}

#if "거주지" not in dict_variable:
    #dict_variable["거주지"] = "전주"

    # 위 조건문은 거주지 라는 키가 없을 때 dict안에 넣어주는 것을 의미
    # 거주지가 포함되어 입력된 모든 키들이 출력됨

#print(dict_variable)



#list_variable = []

#try:
    #list_variable.append(0)
    #list_variable.append(1)
    #list_variable.append(2)
    #pritn(list_variable[3])

#except:
    #print("에러가 발생했습니다")
    #print("에러의 원인은 무엇인가요?")


""" 
출력 결과
list 내에 추가된 것은 0 1 2기 때문에 3을 출력하라고 명령하면 예외가 발생한다.
그래서 에러가 발생했습니다와 원인은 무엇인가요가 출력된다.
"""



#try:
    #number = 1
    
    #if number == 1
        #print(number)

#except:
    #print("에러가 발생했습니다.")
    #print("에러의 원인은 무엇인가요")

"""
에러 원인
number == 1 뒤에 :가 찍혀있지 않아 오류 발생,
그로 인해 except 문구가 출력되지 않음.

: 사용시 1 그대로 출력 오류 x
"""



#n = 10
#total = 0

#for number in range(0, n + 1):
    #if number % 2 == 0:
        #total += number * 2
    #elif number % 2 == 1:
        #total += number + 1 * 3

#print(total)




dict_variable = {
    "이름:": "정우영",
    "생년월일:": "19000101",
    "회사:": "하이퍼그로스",}

for key, value in dict_variable.items():
    print(key, value)

"""
예측을 작성하세요.
?
"""