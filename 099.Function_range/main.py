#범위를 표현하는 함수 range
#step값을 float로 줄 수 있는 arange()가 있다.

range1 = range(1, 10)
#인자가 2개인 경우 range(start, finish)
range2 = range(1, 100, 2)
#인자가 3개인 경우range(start, finish, step)
range3 = range(10)
#0인자가 1개인 경우 0부터 n까지 표현한다.

print(list(range1))
print(list(range2))
print(list(range3))
