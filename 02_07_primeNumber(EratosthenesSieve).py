#자료구조와 알고리즘 입문
#섹션2. 코드 구현능력 기르기
#06.소수(에라토스테네스의 체) 직접 구현한 코드

import sys

N = int(sys.stdin.readline())

#소수의 정의? 1과 자기 자신의 수로만 나누어 떨어지는 수
#K를 1 ~ K까지 수로 나눴을때, 나머지가 0인수가 2여야함. 
# 예를 들면 4인경우 1로 나누면 나머지는 0, 2로 나누면 나머지가 0 , 3으로 나누면 나머지가 1...3이므로 소수가 아님

'''
def primeReader(x):
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt += 1
    2
    if cnt == 2:
        return 1
    else:
        return 0
'''
cnt = 0
totCnt = 0   

for i in range(1, N + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        totCnt += 1

print(totCnt)

#2가지 방법 모두 시간이 오래 걸린다...