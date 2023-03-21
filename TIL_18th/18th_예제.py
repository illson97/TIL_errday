

# 2789

#W = input()
#word = ''

#for i in W:
    #if i not in 'CAMBRIDGE':
        #word += i
        
#print(word)



# 2675

#n = int(input())

#for _ in range(n):
    #cnt, word = input().split()
    #for i in word:
        #print(i*int(cnt), end='')   
    #print()



# 10988

#word = input()
#palin = list(reversed(word))

#if palin == word:
    #print(1)
#else:
    #print(0)



# 17249

#left, right = input().split("(^0^)")

#print(left.count("@"), right.count("@"))
    



# 2941

#c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
#a = input()

#for i in c :
    #a = a.replace(i, 'a')
#print(len(a))



# 10809

#n = list(map(str, input()))
#for i in range (97,123):
    #for j in range(0, len(n)):
        #a = -1
        #if chr(i) == n[j]:
            #a = j
            #break
    #print(a, end=' ')