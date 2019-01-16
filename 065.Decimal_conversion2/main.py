#진수변환 10 -> 2, 2 -> 10

#10진수를 2진수로 변환하는 함수 bin()
b1 = bin(0)
b2 = bin(4)
ret1 = b1 + b2
#문자열을 합치기 때문에 결과는 0b00b100가 나온다.
print(ret1)

#2진수를 10진수로 변환
a = int(b1,2)
b = int(b2,2)
ret2 = a + b
print(ret2)
