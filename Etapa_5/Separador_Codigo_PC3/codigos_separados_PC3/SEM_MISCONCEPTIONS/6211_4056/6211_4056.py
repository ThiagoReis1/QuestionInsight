num = int(input("digite: "))

contador = 0
while (num != -1):
	if (num >= 100) and (num <= 199):
		contador = contador+1
	num = int(input("digite: "))
print(contador)