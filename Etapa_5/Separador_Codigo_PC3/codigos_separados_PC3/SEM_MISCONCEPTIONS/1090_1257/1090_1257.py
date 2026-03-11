# Mayara Soares
# 30 - 06 - 2016
# Av 2  Ex 1

compra_1 = float(input("digite o valor da compra: "))
compra_2 = float(input("digite o valor da compra: "))
compra_3 = float(input("digite o valor da compra: "))
compra_4 = float(input("digite o valor da compra: "))
limite_cartao = float(input("digite o limite do cartao: "))

valor_total_compras = (compra_1 + compra_2 + compra_3 + compra_4)
print(round(valor_total_compras, 2))

if(valor_total_compras <= limite_cartao):
	print("Sim")
	
else:
	print("Nao")
	
