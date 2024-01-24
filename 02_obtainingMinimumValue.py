#자료구조와 알고리즘 입문
#섹션2. 코드 구현능력 기르기
#선수지식 - 최소값 구하기

arr = [5, 3, 7, 9, 2, 5, 2, 6]

arrMin = float('inf') 
#'inf'는 무한대를 나타내는 문자열, 이를 float()함수에 넣어 부동소수점 무한대값을 형성
for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)

#02 : for x in range를 사용
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf') 
#'inf'는 무한대를 나타내는 문자열, 이를 float()함수에 넣어 부동소수점 무한대값을 형성
for x in range(len(arr)):
    if x < arrMin:
        arrMin = x
print(arrMin)

#03 : 첫번째 값인 arr[0]을 사용
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = arr[0]
for i in range(1, len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)