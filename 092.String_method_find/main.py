#문자열에서 특정 문자 위치 찾는 메소드
#메소드 = 'find'

txt = 'The Internet of Things'

result1 = txt.find('of')
result2 = txt.find('Th')
result3 = txt.find('Th', 10)    #10번째 이후부터 'Th'를 찾음
result4 = txt.find('Hello')

print(result1)
print(result2)
print(result3)
print(result4)                  #해당 문자나 문자열을 찾지 못하면 -1를 return함
