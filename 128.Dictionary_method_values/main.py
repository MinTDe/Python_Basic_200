#dictionary에서 값만 추출하기
#메소드 'value'

ID = {'mint' : 123, 'MINT' : 321}

vals = ID.values()
print(vals)

vals_list = list(vals)
vals_sum = sum(vals_list)
print(vals_sum)
