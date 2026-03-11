V = float(input("Premio: "))
M = float(input("Saque: "))
j = float(input("Taxa de juros: "))


saldo = V
tempo = 0

if(V > 0 and M > 0 and j > 0):
	
	while(saldo < V + ((V * 20 / 100))):
		saldo = round((saldo + ( saldo * j)/100)-M, 2)
		tempo = tempo + 1
	print(tempo)
		
else:
	print("Dados incorretos")