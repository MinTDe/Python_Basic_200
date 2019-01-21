#문자열을 특정 문자로 분리하기
#메소드 split

url = 'https://github.com/MinTDe/Python_Basic_200/graphs/traffic'
log = 'name:MinTde age:209 sex:unkown nation:korea'

parsing = url.split('/')    #'/'를 구분자로 문자열을 분리함
print(parsing)

parsing2 = log.split()      #split()에 인자가 없으면 default로 공백을 구분자로 인식
#print(parsing2)

for data in parsing2:
    data1, data2 = data.split(':')
    print('%s -> %s'%(data1, data2))
