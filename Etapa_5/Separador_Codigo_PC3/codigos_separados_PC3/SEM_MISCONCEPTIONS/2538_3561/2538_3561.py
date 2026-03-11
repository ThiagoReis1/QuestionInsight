S=float(input("valor do sitio:"))
D=float(input("valor do deposito: "))
M=float(input("valor mensal fixo:"))
j=float(input("taxa de juros:"))
tempo=0
saldo=D
if(S>0)and(D>0)and(M>0)and(j>0):
	while(saldo<S):
		saldo= saldo+ saldo*(j/100)
		saldo = round(saldo,2)
		saldo=saldo+M
		tempo= tempo+1
	print(tempo)
else:
	print("Dados incorretos")