#문자열에서 특정 문자 위치 찾는 메소드
#메소드 = 'find'

txt = 'The Internet of Things'

result1 = txt.find('of')
result2 = txt.find('Th')
result3 = txt.find('Th', 10)

print(result1)
print(result2)
print(result3)
