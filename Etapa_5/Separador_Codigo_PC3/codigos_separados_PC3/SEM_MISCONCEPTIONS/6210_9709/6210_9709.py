num = int(input("Digite num: "))
contador = 0
while num != -1:
	if num >= 35 and num <= 95:
		contador += 1
	num = int(input("Digite num: "))
print(contador)