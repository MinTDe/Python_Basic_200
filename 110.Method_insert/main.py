#특정위치에 리스트 요소를 삽입하는 메소드는
#메소드 'insert'

korea = ['Seoul', 'Busan', 'Incheon']

print(korea)

pos = korea.index('Busan')
korea.insert(pos, 'Jeonju')

print(korea)
