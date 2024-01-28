#자료구조와 알고리즘 입문
#섹션2. 코드 구현능력 기르기
#08.뒤집은 소수 직접 구현한 코드

import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

# 뒤집는 함수
def reverse(x):
    strX = str(x)
    lenX = len(strX)
    revX = []
    for i in range(lenX - 1, -1, -1):
        if strX[i] != 0:
            revX.append(strX[i])

    joinX = (''.join(revX))

    return int(joinX)

# 소수인지 확인하는 함수
def isPrime(x):
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt += 1
    
    if cnt == 2:
        return 1

for i in range(N):
    if isPrime(reverse(A[i])) == 1:
        print(reverse(A[i]), end = ' ')
    
