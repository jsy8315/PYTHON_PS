#자료구조와 알고리즘 입문
#섹션2. 코드 구현능력 기르기
#K번째 수
import sys
T = int(sys.stdin.readline())
A = []
C = []

for i in range(T):
    N, s, e, k = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = A[s - 1 : e]
    B.sort()
    print("#%d %d" %(i + 1, B[k - 1]))
    print("%d살입니다." %(i))


# %d, %s, %f 정수, 스트링, 실수