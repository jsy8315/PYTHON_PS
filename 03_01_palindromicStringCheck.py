#자료구조와 알고리즘 입문
#섹션3. 탐색 & 시뮬레이션(string, 1차원, 2차원 리스트 탐색)
# 01. 회문 문자열 검사

import sys
N = int(sys.stdin.readline())

A = [0] * N

for i in range(N):
    A[i] = sys.stdin.readline().strip().upper()

print(A)

for i in range(N):
    cnt = len(A[i]) // 2
    for j in range(len(A[i]) // 2):
        if A[i][j] == A[i][len(A[i]) - j -  1]:
            cnt -= 1
        
    if cnt == 0:
        A[i] = "#" + str(i + 1) + " YES"
    else:
        A[i] = "#" + str(i + 1) + " NO"
    
for i in range(N):
    print(A[i])