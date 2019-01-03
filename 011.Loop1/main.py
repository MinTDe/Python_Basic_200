#반복분 예제
print('Using List')
list_data = [1,2,3,4,5]

for i in list_data:
    print(i)
#for문의 구조
#for 변수 in 범위 :
#범위로 사용가능한 자료들은 문자열, 리스트, 튜플, 사전, range()가 대표적이다.

#문자열을 사용한 예시
print('Using String')
string_data = 'abcdef'

for i in string_data :
    print(i)

#사전을 사용한 예시
print('Using Dictionary')
dic_data = {'a':'e', 2:'b', 100:'c'}

for i in dic_data :
    print(i)

#range()를 사용한 예시
print('Using range()')

for i in range(10) :
    print(i)
