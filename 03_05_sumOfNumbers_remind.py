#자료구조와 알고리즘 입문
#섹션3. 탐색 & 시뮬레이션(string, 1차원, 2차원 리스트 탐색)
#05. 수들의 합, 강의 내용 복습

import sys

N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))

lt = 0
rt = 1

tot = A[0]
cnt = 0

while True:
    if tot < M:
        if rt < N:
            tot += A[rt]
            rt += 1
        else:
            break
    elif tot == M:
        cnt += 1
        tot -= A[lt]
        lt += 1
    else:
        tot
        lt += 1

print(cnt)


