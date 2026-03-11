qi = float(input("Quantia inicial: "))
tempo = int(input("meses investido: "))
juros = 1.2
saldo = qi 

cont = 0
while(cont < tempo):
		rend = saldo * juros
		saldo =  saldo + rend
		print(round(saldo, 2 ))
		cont = cont + 1 