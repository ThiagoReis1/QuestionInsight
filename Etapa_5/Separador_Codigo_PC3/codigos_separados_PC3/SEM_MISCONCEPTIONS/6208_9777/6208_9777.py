numero = int(input("Digite um numero (-1 para encerrar): "))

numeros_da_sorte = 0
while numero != -1:
	if numero>=51 and numero <= 75:
		numeros_da_sorte += 1
	numero = int(input(""))
print(numeros_da_sorte)