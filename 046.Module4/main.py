#모듈 사용 예시
#모듈 생성 예시
#패키지 사용 예시
#패키지 생성 예시

#import package_name.module_name
#import mypackage.mylib
from mypackage import mylib
from mypackage.mylib import reverse

#import module_name
#import sleep.time
from time import  sleep

#time.sleep(1)
sleep(1)

#ret1 = mypackage.mylib.add(1,3)
ret1 = mylib.add(1, 3)
print(ret1)

#ret2 = mypackage.mylib.reverse(1, 6, 9)
ret2 = reverse(1,3,5)
print(ret2)
