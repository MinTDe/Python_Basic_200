#모듈 사용 예시
#모듈 생성 예시
#패키지 사용 예시
#패키지 생성 예시
#from ~ import

from mypackage import mylib

from mypackage.mylib import reverse
#from package_name import module_name


from time import  sleep
#from module_name import function_name

#time.sleep(1)
sleep(1)

ret1 = mylib.add(1, 3)
print(ret1)

ret2 = reverse(1,3,5)
print(ret2)
