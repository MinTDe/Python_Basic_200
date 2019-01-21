#filter함수 사용 예시
#소수만 뽑아내는 함수
#filter(특정조건의 값을 추출하는 함수, 반복가능한 자료)

def getPrime(x):
    if x % 2 == 0:
        return

    for i in range(3, int(x/2), 2):
        if x % i == 0:
            break
    else:
        return x

list_data = [5,117,119,123453,11113]
ret = filter(getPrime,list_data)
print(list(ret))
