valor = float(input("digite o valor de x: "))

if(valor <= -1) or (valor >= 1):
	print(valor)

elif(valor > -1 and valor < 0) or (valor > 0 and valor < 1):
	print(round(abs(valor),2))

elif(valor == 0):
	print(0)
