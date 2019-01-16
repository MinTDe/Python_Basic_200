#진수변환 10 -> 16, 16 -> 10

#10진수를 16진수로 변환하는 함수 hex()
h1 = hex(0)
h2 = hex(4)
ret1 = h1 + h2
#문자열을 합치기 때문에 결과는 0x00x4가 나온다.
print(ret1)

#16진수를 10진수로 변환
a = int(h1,16)
b = int(h2,16)
ret2 = a + b
print(ret2)
