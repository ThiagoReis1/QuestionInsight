quantInicial = int(input("Entre com o numero: "))
quantDia = int(input("Entre com o numero: "))
quantNoite = int(input("Entre com o numero: "))
 
#quantNoite = quantInicial - quantDia

dias = 0

while (quantInicial > 0):
	quantInicial = quantInicial + (quantNoite - quantDia)
	dias = dias + 1
print(dias)