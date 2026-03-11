# Rodrigo de Oiveira Brasil Ferreira - 21602328
# Avaliacao 2 - grupo 2
# 14 / 07 / 2016
# Entrada
num = int(input("digite um numero: "))
x1 = num // 100
x2 = num % 100

if(num == (x1 ** 2) + (x2 ** 2)):
	print((x1 ** 2) + (x2 ** 2), "atende a propriedade")
else:
	saida = (x1 ** 2) + (x2 ** 2)
	print(saida)