#문자열이 문자 또는 숫자로만 이루져있는 검사하는 메소드
#메소드 = 'isalnum'

txt1 = "Hello?"
txt2 = "Hello World!"
txt3 = "id123"

result1 = txt1.isalnum() #'?'가 있기 때문에 결과 값은 false
result2 = txt2.isalnum() #' '와 '!가 있기 때문에 결과 값은 false'
result3 = txt3.isalnum()

print(result1)
print(result2)
print(result3)
