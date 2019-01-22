#정렬 함수
#함수 'sorted'

str = 'qazwsxedcrfvtgbyhnujmikolp'
ret1 = sorted(str)
ret2 = str
print(ret1)

ret1 = ' '.join(ret1)
ret2 = ' '.join(sorted(ret2, reverse = True))
#reverse = True는 내림차순 정렬을 의미
print(ret1)
print(ret2)
