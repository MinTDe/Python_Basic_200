#2, 8, 16진수를 10진수로 변환시키기
b_num =  0b11110000
o_num = 0o360
h_num = 0xf0

b_str = '0b11110000'
o_str = '0o360'
h_str = '0xf0'

b1 = int(b_num)
b2 = int(b_str,2)#2대신 0도 가능

o1 = int(o_num)
o2 = int(o_str,8)#8대신 0도 가능

h1 = int(h_num)
h2 = int(h_str,16)#16대신 0도 가능



print(b1)
print(b2)
print(o1)
print(o2)
print(h1)
print(h2)
