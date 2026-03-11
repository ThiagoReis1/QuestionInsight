v1 = float(input("valor da compra: "))
v2 = float(input("valor da compra: "))
v3 = float(input("valor da compra: "))
limite = float(input("limite do cartao: "))
valor_total = v1 + v2 + v3
print(round(valor_total, 2))
if (valor_total <= limite):
	print("Nao ultrapassou")
else:
	print("Ultrapassou")
	
