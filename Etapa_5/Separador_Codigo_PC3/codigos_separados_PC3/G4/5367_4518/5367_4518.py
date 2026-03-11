cpf = eval(input())
acum = 0
cont = 0

while cont < 9:
	acum += cpf[cont] * (cont + 1)
	cont += 1
	
print(acum % 11)