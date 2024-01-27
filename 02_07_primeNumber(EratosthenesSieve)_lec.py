#자료구조와 알고리즘 입문
#섹션2. 코드 구현능력 기르기
#소수(에라토스테네스의 체), 강의 내용

import sys

n = int(sys.stdin.readline())

ch = [0] * (n + 1)
cnt = 0

for i in range(2, n + 1):
    if ch[i] == 0:
        cnt += 1
        for j in range(1, n + 1, i):
            ch[j] = 1

print(cnt)