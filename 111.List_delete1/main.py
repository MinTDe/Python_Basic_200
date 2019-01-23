#리스트에 있는 내용을 삭제하는 방법

list_data1 = ['a', 'b', 'c']

print(list_data1)

del list_data1[0]
print(list_data1)

#삭제를하면 요소들이 앞으로 한 칸씩 이동한다.
del list_data1[0]
print(list_data1)
print(list_data1[0])
