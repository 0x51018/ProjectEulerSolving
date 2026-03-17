# 세자리수 2개의 곱이니까 100*100 이상, 999*999 이하. 즉 10000 <= ans < 998001
# 걍 다해보기

def isPalindrome(num):
    flag, strnum = True, str(num)
    for i in range(len(strnum)): 
        if strnum[i] != strnum[-1-i]: flag = False
    return flag

pal = []
for x in range(100, 1000):
    for y in range(x, 1000):
        if isPalindrome(x*y): pal.append(x*y)
print(sorted(pal)[-1])