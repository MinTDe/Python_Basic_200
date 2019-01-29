#readlines()는 파일을 한 번에 다 읽고 한줄 씩 리턴한다.
#138번 예제랑 다르게 나옴
f = open('test.txt', 'r')
lines = f.readlines()

for line_num in enumerate(lines):
    print('%s %s' %(line_num, lines), end="")
f.close()
