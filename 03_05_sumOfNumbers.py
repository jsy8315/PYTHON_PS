#자료구조와 알고리즘 입문
#섹션3. 탐색 & 시뮬레이션(string, 1차원, 2차원 리스트 탐색)
#05. 수들의 합

import sys

N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))

sum = [0] * N
cnt = 0

for i in range(N):
    if A[i] > M:
        break
    else:
        for j in range(i, N):
            sum[i] = sum[i] + A[j]
            if sum[i] == M:
                cnt += 1
                break

print(cnt)