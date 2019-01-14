#Class 소멸자 예시
class Class:
    def __init__(self):
        self.hello = 'Hello'
    #Class 소멸시 출력됨
    def __del__(self):
        print('Delete Class')

obj = Class()
print(obj.hello)
del obj
#print(obj.hello)
