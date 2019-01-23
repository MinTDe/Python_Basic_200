#dictionary에서 특정 키 존재 유무 확인하기
#명령어 in

ID = {'mint' : 123, 'MINT' : 321}

id = input('input your id : ')
if id in ID:
    print('your password is %d' %ID[id])
else:
    print('No your id in DB')
