#Class 선언 예시
class Class :
    def __init__ (self) :
        self.param2 = 'Hallo'
        self.var = 'Hello'

    def Hello(self) :
        param1 = 'Hi'
        self.param2 ='Hallo'
        print(param1)
        print(self.var)
        print(self.param2)

obj = Class()
print(obj.var)
obj.Hello()
