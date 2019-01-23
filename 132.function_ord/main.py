#문자를 코드로 변환시키는 함수
#함수 = 'ord'

ch = input('input char : ')

if len(ch) != 0:
    ch = ch[0]
    chv = ord(ch)
    print('%s : %d : %s' %(ch, chv, hex(chv)))
