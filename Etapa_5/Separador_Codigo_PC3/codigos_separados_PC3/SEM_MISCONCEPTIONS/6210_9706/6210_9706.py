num = int(input())
contador = 0

while num > 0:
	if num >= 35 and num <= 95:
		contador += 1
	num = int(input())
print(contador)