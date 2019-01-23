#리스트를 (인덱스, 요소)로 뽑아내는 함수
#함수 'enumerate'

alpahbet_list = ['q', 'a', 'z', 'w', 'e', 'r', 's', 'd', 'f', 'x', 'c', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u', 'i', 'o', 'j', 'k', 'l', 'm', 'p']

alpahbet_list.sort()

list = list(enumerate(alpahbet_list))
print(list)
