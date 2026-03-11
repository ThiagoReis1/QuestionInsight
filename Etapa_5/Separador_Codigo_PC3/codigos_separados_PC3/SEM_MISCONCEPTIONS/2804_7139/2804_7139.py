#Entradas

deposito = float(input("Deposito:"))
meses = int(input("Meses:"))

cont = 1
valor = deposito

while (cont <= meses):
	rendimento = (valor * (1/100)) 
	valor = valor + rendimento
	cont = cont + 1
	print(round(valor,2))