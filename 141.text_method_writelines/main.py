# method writelines()

count = 1
data = []

print('save = [enter]')

while True:
    text = input('[%d]file input' %count)
    if text == "":
        break
    data.append(text + '\n')
    count += 1

f = open('test.txt', 'w')
f.writelines(data)
f.close()
