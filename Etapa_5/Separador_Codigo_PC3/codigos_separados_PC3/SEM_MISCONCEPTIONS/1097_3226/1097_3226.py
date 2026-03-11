numero= str(input())

senha1= int(numero[0])*100 + int(numero[1])*10 + int(numero[2])*1
senha2= int(numero[3])*100 + int(numero[4])*10 + int(numero[5])*1
calculo = (senha1 - senha2) ** 2
print(senha1)
print(senha2)
if (numero == calculo):
	print("atende")
	print(numero)
else:
	print("nao atende")
	print(numero)