#함수의 리턴 예시
def reverse(x, y, z) :
    return z, y, x

tuple1 = reverse(1, 2, 3)       #return 값이 많으 때는 Tuple로 return값을 만들어 return한다.
print(tuple1)

a, b, c = reverse(1, 2, 3)      #개별적으로 return값을 넣을 수 있다.
print(a);print(b);print(c)
