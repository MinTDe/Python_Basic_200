#지역변수와 전역 변수
str1 = 'Global Variable'        #전역변수

def func1() :
    str1 = 'Local Variable'     #지역변수
    print(str1)                 #함수 내부에서는 지역변수가 우선 순위

func1()
print(str1)
