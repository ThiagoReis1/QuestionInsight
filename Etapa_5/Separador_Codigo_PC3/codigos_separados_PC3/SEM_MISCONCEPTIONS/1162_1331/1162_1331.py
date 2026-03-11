valor1 = float(input("Valor do premio:"))
taxa = input("taxa de juros:")
valor2 = float(input("Valor Retirado:"))
cont = 0

while(valor1==0):
	valor1 = valor1 * taxa
	valor2 = valor1 - valor2
	t = 1 + cont
print(t)