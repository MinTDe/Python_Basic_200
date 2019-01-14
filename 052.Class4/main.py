class Class :
    #Class의 인스턴스 객체가 생성될 때 자동적으로 호출되는 메소드
    def __init__(self) :
        self.hello = 'Hello'
        print('Make Instance')

obj = Class()
print(obj.hello)
