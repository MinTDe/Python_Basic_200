#문자열을 바이트 객체로 바꾸는 메소드
#메소드 'encode'
u_txt = 'I love python'
b_txt = u_txt.encode()

print(u_txt)
print(b_txt)            #바이트 객체로 변환되었기 때문에 b'I love python'라고 출력이 된다.

ret1 = 'I' == u_txt[0]
ret2 = 'I' == b_txt[0]  #바이트 객체이기 때문에 _txt[0]은 'I'가 아니라 73이다

print(ret1)
print(ret2)             #결과 값은 False
