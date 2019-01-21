#문자열을 수치형 자료로 변환하기

num_str = input('inpu number : ')

try:
    num_data = int(num_str)
    print('Your input number is <%d>' %num_data)
except:
    try:
        num_data = float(num_str)
        print('Your input number is <%f>' %num_data)
    except:
        print('----input number----')
