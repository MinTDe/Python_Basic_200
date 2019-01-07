#비트 연산자 예시
bit1 = 0x31
bit2 = 0x0
#hex정수 값을 소문자 16진수 문자열로 0x 값과 함께 출력
print(hex(bit1 & bit2));    #비트간 and 연산
print(hex(bit1 | bit2));    #비트간 or 연산
print(hex(bit1 ^ bit2));    #비트간 xor 연산
print(hex(~bit2));          #1의 보수를 취함
print(hex(bit1 << 1));      #비트를 n만큼 왼쪽 이동
print(hex(bit1 >> 1));      #비트를 n만큼 오른쪽 이동
