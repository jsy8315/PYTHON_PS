#자료구조와 알고리즘 입문
#섹션2. 코드 구현능력 기르기
#09. 주사위 게임

import sys

N = int(sys.stdin.readline())

B = [0] * N

'''
A = [3, 8, 5, 7]
print(sorted(A, reverse = True))
print(A)
print(A.sort(reverse = True))
print(A)
'''
for i in range(N):
    A  = list(map(int, sys.stdin.readline().split()))
    A.sort(reverse = True)

    if A[0] == A[1]:
        if A[1] == A[2]:
            B[i] = 10000 + (A[0] * 1000)
        else:
            B[i] = 1000 + (A[0] * 100)
    else:
        if A[1] == A[2]:
            B[i] = 1000 + (A[1] * 100)
        else:
            B[i] = A[0] * 100

print(max(B))

    