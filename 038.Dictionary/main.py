#dictionary사용 예시
def hello():
    print('Hello')

#dictionary는 인덱스 값으로 접근할 수 없다. dictionary는 키:값 쌍이 하나의 요소고 키로 접근해야된다.
dict1 = {'a':1, 'b':2, 'c':hello}

print(dict1)
dict1['c']()

dict1['d'] = 5
print(dict1)
