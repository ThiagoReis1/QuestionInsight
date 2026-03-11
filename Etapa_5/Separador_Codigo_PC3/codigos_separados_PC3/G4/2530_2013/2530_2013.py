#variaveis
D=float(input("deposito:"))
TF=float(input("tarifa mensal:"))
J=float(input("juros mensal:"))
k=(D+(D*15/100))

#variavel contadora
tempo=0

#
if (D>0 and TF>0and J>0):
	while (D<=k):
		D=round(D+(D*J/100)-TF,2)
		tempo=tempo+1	
	print(tempo)
else:
	print("Dados incorretos")
		