#클래스 메소드 이해
class Class:
    def __init__(self) :
        self.hello = 'Hello'
    #첫 번째 인자는 self가 있어야 된다.
    def Hello(self):
        print(self.hello)

obj = Class()
obj.Hello()
