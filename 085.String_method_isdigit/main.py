#문자열이 숫자인지 검사하는 메소드
#메소드 = 'isdigit'

txt1 = '112'
txt2 = '112-119'        #'-' 기호가 들어가있기 때문에 false가 출력된다.
txt3 = 'Hello World!'   #문자로 이루어져 있는 문자열이기 때문에 false가 출력된다.

result1 = txt1.isdigit()
result2 = txt2.isdigit()
result3 = txt3.isdigit()

print(result1)
print(result2)
print(result3)
