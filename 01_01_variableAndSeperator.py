#변수 타입
a = 12.123456789123456789123456789
print(a)
#실수형은 8바이트까지만 저장 가능,123456781234567까지가 8바이

##seperator
a, b, c = 1, 2, 3
print(a, b, c, sep='&')
#각 변수 사이를 , 로 지정

print(a, b, c, sep='\n')
#각 변수 사이를 \n로 지정, 줄바꿈
# *프린터는 자동으로 줄바꿈이 존재함. 

#줄바꿈말고 옆으로 옮기기 : end
print(a, end = '+')
print(b, end = '+')
print(c)
