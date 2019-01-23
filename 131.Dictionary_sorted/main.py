#dictionary에서 sorted사용하기

def f1(x):
    return x[0]

def f2(x):
    return x[1]


ID = {'mint' : 123, 'MINT' : 321, 'asd' : 125 , 'jhfg' : 756, 'rytu' : 124, 'ptrg' : 4976}

ret1 = sorted(ID)
print(ret1)
#>>>['MINT', 'asd', 'jhfg', 'mint', 'ptrg', 'rytu']

ret2 =sorted(ID.items())
print(ret2)


ret2 =sorted(ID.items(), key = f1)      #키를 기준으로 오름차순
print(ret2)

ret2 =sorted(ID.items(), key = f2)      #값을 기준으로 오름차순
print(ret2)
