#자료구조와 알고리즘 입문
#섹션2. 코드 구현능력 기르기
#K번째 약수
import sys
N, K = map(int, sys.stdin.readline().split())
A = []
for i in range(1, N + 1):
    if N % i == 0:
        A.append(i)

if len(A) < K:
    print(-1)
else:
    print(A[K - 1])
    

#예시코드
'''
import sys
N,K = map(int, sys.stdin.readline().split())
cnt = 0
for i in range(1, N + 1):
    if N % i == 0:
        cnt += 1
    if vnt == k:
        print(i)
        break
else:
    print(-1)

if-else뿐만 아니라
for-else도 존재한다
''' 

