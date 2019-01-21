#1byte에서 상위 4bit 추출
a = 107 # 0x6b
b = (a>>4) & 0x0f
print(b)
