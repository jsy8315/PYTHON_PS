# 자료구조와 알고리즘 입문
# 섹션2. 코드 구현능력 기르기
# 주사위게임, 강의 내용

import sys

n = int(sys.stdin.readline())
res = 0

for i in range(n):
    tmp = int(sys.stdin.readline().split())
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and b == c:
        money = 10000 + a * 1000
    elif a == b or a == c:
        money = 1000 + (a * 100)
    elif b == c:
        money = 1000 + (b * 100)
    else:
        money = c* 100
    if money > res:
        res = money

print(money)