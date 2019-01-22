#리스트에서 짝수만 추출하기
#사용 '::'
#list[n :: x] -> n번째 부터 x만큰 step하겠다는 의미
list_data = list(range(1, 21))
another_list = list_data[1::2]
print(another_list)
