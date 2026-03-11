compra1 = float(input("insira o valor da compra: "))
compra2 = float(input("insira o valor da compra: "))
compra3 = float(input("insira o valor da compra: "))
limite = float(input("insira o limite: "))
valor = compra1 + compra2 + compra3
print(valor)

if(valor <= limite):
	print("Nao ultrapassou")

else:
	print("Ultrapassou")

