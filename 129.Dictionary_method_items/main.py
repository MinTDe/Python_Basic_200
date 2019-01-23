#dictionary에서 모든 요소 추출하기
#메소드 'items'

ID = {'mint' : 123, 'MINT' : 321}

items = ID.items()
print(items)

for item in items:
    print(item)
