#Class 상속 이해하기
class Add :
    def add(self, a, b) :
        return a + b

#class 자식클래스(부모클래스)
#다중상속도 가능하다.
class Calculator(Add) :
    def sub(self, a, b) :
        return a- b

obj = Calculator()

print(obj.add(1,2))
print(obj.sub(1,2))
