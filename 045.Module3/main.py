#모듈 사용 예시
#모듈 생성 예시
#패키지 사용 예시
#패키지 생성 예시

#import package_name.module_name
import mypackage.mylib

#import module_name
import time

time.sleep(1)

ret1 = mypackage.mylib.add(1,3)
print(ret1)

ret2 = mypackage.mylib.reverse(1, 6, 9)
print(ret2)
