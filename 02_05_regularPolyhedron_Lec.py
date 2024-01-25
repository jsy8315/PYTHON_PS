#자료구조와 알고리즘 입문
#섹션2. 코드 구현능력 기르기
#정다면체, 강의 내용

import sys
n, m = map(int, sys.stdin.readline().split())
cnt = [0] * (n + m + 3) #n + m 까지만 해도 되지만...혹시 모르니 3을 넣자
max = -2147000000

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1

for i in range(n + m + 1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n + m + 1):
    if cnt[i] == max:
        print(i, end = ' ')