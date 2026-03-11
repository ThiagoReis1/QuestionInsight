d= float(input("Deposito: "))
tf= float(input("Tarifa mensal: "))
j= float(input("Taxa de juros: "))


tempo= 0
saldo= d



if d > 0 and tf > 0 and j > 0:
	while (saldo < (d*1.5 )):
		saldo= saldo+(j/100)
		saldo= saldo - tf
		saldo= round(saldo, 2)
		tempo= tempo + 1
	
else:
		print("Dados incorretos")
print(tempo)


	