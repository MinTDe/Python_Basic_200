#문자열 합치기 예시
#'*' 기호를 통해서도 문자열을 합칠 수 있다.
str1 = 'HHH'
str2 = "YYY"

str3 = (str1 + str2 + str1*4) * 4
print(str3)
