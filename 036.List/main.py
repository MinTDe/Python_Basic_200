#리스트 예시
def hello():
    print("Hello")

list1 = [1,2,3,4,5]
#list에는 함수도 넣을 수 있다.
list2 = [list1, hello]

print(list1)
print(list2)
list2[1]()
