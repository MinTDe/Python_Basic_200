#Class 선언 예시
class Class :               #class class_name :
    var = 'Hello'           #class 멤버 정의
    def Hello(self) :       #class 메소드 정의
        print(self.var)

obj = Class()
print(obj.var)
obj.Hello()
