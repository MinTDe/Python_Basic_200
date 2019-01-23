#문자열을 실행시켜보자
#함수 'eval'

expr1 = '2 + 3'
expr2 = "round(3.7)"

print(expr1, expr2)

ret1 = eval(expr1)
ret2 = eval(expr2)

print(ret1, ret2)
