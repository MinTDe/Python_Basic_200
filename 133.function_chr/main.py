#코드값에 대응하는 문자 얻기

val = input('input number : ')
vals = int(val)
try:
    ch = chr(vals)
    print('%d : %s' %(vals, ch))
except ValueError:
    print('no character in data')
