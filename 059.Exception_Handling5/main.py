#예외처리 예시
#try ~ except 특정 예외
import time
count = 1

try:
    while True:
        print(count)
        count += 1
        time.sleep(1)
except KeyboardInterrupt: # control-c 입력되면 발생되는 오류
    print('finish')
