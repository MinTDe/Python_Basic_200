#리스트에 요소를 추가할 수 있는 메소드
#메소드 append
#'append' 메소드는 list 맨 뒤에 메소드를 추가시킨다.

list_data1 = ['a', 'b', 'c']

print(list_data1)

for i in range(3):
    txt = input('input character : ')
    list_data1.append(txt)

print(list_data1)
