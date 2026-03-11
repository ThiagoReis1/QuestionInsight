C_F = input("informe C se for coxinha ou E se for esfirra: ").upper()
quant = int(input("quantidade pedidas: "))
sucos = int(input("informe a quantidade de sucos pedidos: "))

if C_F == "C":
	total = quant * 2 + sucos *6
else:
	total = quant * 4.50 + sucos * 6
print(round(total, 2))