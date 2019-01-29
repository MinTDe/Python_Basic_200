#read()는 파일 전체를 읽는다.
f = open('test.txt','r') # test파일을 'r'모드로 오픈 -> 오픈한 파일 객체를 f로 둔다.
data = f.read()
print(data)
f.close()               #파일에 대한 처리가 끝나면 파일 객체를 close()를 사용해서 닫느다.
