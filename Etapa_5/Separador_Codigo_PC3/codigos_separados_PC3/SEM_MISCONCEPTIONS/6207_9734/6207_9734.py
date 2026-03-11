contador = 0
num = int(input("num"))
while num != -1:
	if 26 <= num <= 50:
		contador += 1
		num = int(input("numero"))
print(contador)