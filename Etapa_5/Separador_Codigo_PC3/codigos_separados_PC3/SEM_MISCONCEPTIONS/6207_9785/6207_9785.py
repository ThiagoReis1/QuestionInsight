contador = 0
num = int(input())

while num != -1:
	if 26 <= num <= 50:
		contador += 1
	num = int(input())
print(contador)