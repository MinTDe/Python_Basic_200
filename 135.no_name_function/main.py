#이름없는 한줄 함수
#'lambda'
#lambda 인자, 인자... : code

add = lambda x, y : x + y
sum = add(1, 3)
print(sum)

ID = {'mint' : 123, 'MINT' : 321, 'asd' : 125 , 'jhfg' : 756, 'rytu' : 124, 'ptrg' : 4976}

ret2 = sorted(ID.items(), key = lambda x: x[0])
print(ret2)

ret2 = sorted(ID.items(), key = lambda x: x[1])
print(ret2)
