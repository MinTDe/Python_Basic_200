#함수 인자 사용 예시
def add_txt1(str1, str2 = 'World!') :
    print(str1 + ' ' + str2)

add_txt1('Hello')

#인자이름을 명시하고 값을 대입했을 때 인자의 순서는 무시된다.
#'키워드 인자에 의한 값 전달 방법'
add_txt1(str2 = 'Hello', str1 = 'World!')

#*args는 가변인자고 이름앞에 *을 붙인다.
#args는 함수 내부에서 튜플로 처리된다.
def add1(*args):
    print(args)

#**c는 가변인자고 이름 앞에 **을 붙인다.
#c는 함수 내부에서 사전으로 처리된다.
def add2(a,b, **c) :
    print(c)
    #print(c[abc])

add1()
add1(3,5,1,5)
add2(10,20)
add2(10,20,abc = 20, bcd = 30)
