#for~break구문 예시
#for문이 끝까지 반복해야 else구문이 작동함
data_list = [1,2,3,4,5]

for i in data_list :
    if i == 3 :
        continue
    else :
        print(i)
else :
    print('Finish')

for i in data_list :
    print(i)
    break
else :
    print('Finish')
