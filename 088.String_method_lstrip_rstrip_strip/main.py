#문자열 공백을 제거하는 함수
txt = ' margin '

result1 = txt.lstrip()  #왼쪽 공백을 제거
result2 = txt.rstrip()  #오른쪽 공백을 제거
result3 = txt.strip()   #양족 공백을 제거

print('<'+result1+'>')
print('<'+result2+'>')
print('<'+result3+'>')
