#자료구조와 알고리즘 입문
#섹션2. 코드 구현능력 기르기
#K번째 큰 수

import sys

N, K = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))

C = []

#3중 for 문?
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
           D =  A[i] + A[j] + A[k]
           C.append(D)
       
B = sorted(C, reverse=True)

#K번째로 큰 값은 아래와 같은 코드로 구할 수 있음
cnt = 1

for i in range(1, len(B)):
    if B[i] < B[i - 1]:
        cnt += 1
    if cnt == K:
        print(B[i])
        break

#강의
'''
중복을 제거하는 자료구조 set
ex) res = set()
정수 5를 여러번 넣어도 딱 한번만 들어간다
set에서는 append가 아니라 add
'''

#강의 코드
'''
import sys
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
res = set()
for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            res.add(a[i] + a[j] + a[m])

res = list(res) #set은 sort기능이 없으므로, list로 변환
res.sort(reverse = True)
print(res[k - 1])

'''