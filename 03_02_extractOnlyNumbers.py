#자료구조와 알고리즘 입문
#섹션3. 탐색 & 시뮬레이션(string, 1차원, 2차원 리스트 탐색)
# 02. 숫자만 추출

import sys

A = str(sys.stdin.readline().strip())

size = len(A)

B = []

for i in range(size):
    if A[i] == '0':
        B.append(int(A[i]))
    if A[i] == '1':
        B.append(int(A[i]))
    if A[i] == '2':
        B.append(int(A[i]))
    if A[i] == '3':
        B.append(int(A[i]))
    if A[i] == '4':
        B.append(int(A[i]))
    if A[i] == '5':
        B.append(int(A[i]))
    if A[i] == '6':
        B.append(int(A[i]))
    if A[i] == '7':
        B.append(int(A[i]))
    if A[i] == '8':
        B.append(int(A[i]))
    if A[i] == '9':
        B.append(int(A[i]))

sizeB = len(B)

C = []

for i in range(sizeB):
    if len(C) == 0 and B[i] == 0:
        continue
    else:
        C[0] = C[0] + B[i]

print(C[0])

#뭔가 더 깔끔하게 추출하는 방법이 있지 않을까?