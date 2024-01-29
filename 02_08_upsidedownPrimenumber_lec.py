# 자료구조와 알고리즘 입문
# 섹션2. 코드 구현능력 기르기
# 뒤집은 소수, 강의 내용

import sys

def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x // 2 + 1):  #절반까지만 돌아도 된다
        if x % i == 0:
            return False
    else:
        return True

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline()))

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end = ' ')
