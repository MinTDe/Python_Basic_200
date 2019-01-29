#텍스트 파일을 한줄씩 읽고 출력하기
#readline()은 텍스트 파일을 한 줄 씩 읽는다.
f = open('test.txt', 'r')
line_num = 1
line = f.readline()

while line: #파일의 끝에 읽을 내용이 더 이상 없으면 readline()은 빈 문자열을 리턴
    print('%d %s'%(line_num, line), end ='')
    line = f.readline()
    line_num += 1
f.close()
