numero=int(input("numero fornecido"))
n1=numero//100
reston1=numero%100
n2=reston1
condicao=n1**2+n2**2
if(numero==condicao):
	print("atende")
	print(numero)
else:
	print("nao atende")
	print(numero)