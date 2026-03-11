v=float(input("Indenizacao em R$: "))
c=float(input("Saque fixo: "))
j=float(input("Juros em %: "))

saldo=v
cont=0 #tempo

while saldo>(v/2):
	if v<0 and c<0 and j<0:
		print("Dados incorretos")
	else:
		taxa=c*j+c
		saldo=saldo-taxa
		cont=cont+1
		print(round(cont,2))