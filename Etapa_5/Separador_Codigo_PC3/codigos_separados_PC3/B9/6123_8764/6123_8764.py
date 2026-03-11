c = int(input("Digite a qtd de combustivel: "))

if(c < 17.5):
	z = 0.8
	valor = c + z
elif (c >= 17.5) and (c < 35.0):
	z = 1.3
	valor = c + z
elif(c >= 35.0) and (c < 50.0):
	z = 2.1
	valor = c + z
else:
	z = 3.0
	valor = c + z
print(round(valor, 1))
	