#사전에 요소 추가하는 방법
s_alphabet = ['a', 'b', 'c', 'd', 'e']
l_alphabet = ['A', 'B', 'C', 'D', 'E']

alphabet = {}

for i,k in enumerate(s_alphabet):
        print(i, k)
        val = l_alphabet[i]
        alphabet[k] = val

print(alphabet)
