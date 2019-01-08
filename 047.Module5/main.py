#모듈 사용 예시
#모듈 생성 예시
#패키지 사용 예시
#패키지 생성 예시
#import ~ as

#import module_name as another_name
import mypackage.mylib as mm
import mypackage as mp

ret1 = mp.mylib.add(1, 3)
print(ret1)

ret2 = mm.reverse(1,3,5)
print(ret2)
