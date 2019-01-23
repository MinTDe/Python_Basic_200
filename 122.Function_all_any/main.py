#리스트의 요소들의 참/거짓을 확인하는 함수
#함수 'any' -> 모두 참일 때 True
#함수 'all' -> 모두 거짓일 때 False

list_data1 = [0,1,2,3,4]
list_data2 = [True, True]
#'', "", 0, [], (), {}, None도 False취급을 받는다.
list_data3 = ["", [],{},(), None, False]

print(all(list_data1))
print(all(list_data2))
print(all(list_data3))
print(any(list_data1))
print(any(list_data2))
print(any(list_data3))
