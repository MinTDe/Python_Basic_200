#tuple 사용 예시
def hello():
    print('Hello')

tuple1 = (1,2,3,4)
tuple2 = (tuple1, 'abc')

#tuple에도 요소에 함수를 넣을 수 있음
tuple3 = (tuple2, hello)

#튜플은 요소의 값을 변경할 수 없다.
#tuple1[0] = 3

print(tuple1)
print(tuple2)
print(tuple2[0][0])
tuple3[1]()
