#-*- coding: utf-8 -*-
#리스트에서 특정 요소 위치 구하는 메소드
#메소드 'index'
#index(요소)
#index(요소, n) n번째 위치부터 찾겠다는 의미
#index를 사용해 요소 변경하기

korea = ['Seoul', 'Busan', 'Incheon']
country = 'Seoul'

pos = korea.index(country)
korea[pos] = '서울'

print(korea[pos])
