contador = 0
n_sorte = int(input("digite o numero: "))
while n_sorte != -1:
	if n_sorte >= 51 and n_sorte <= 75:
		contador += 1
		n_sorte = int(input("digite o numero: "))
	else:
		n_sorte = int(input("digite o numero: "))
print(contador)