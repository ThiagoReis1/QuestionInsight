from numpy import *

prod_comprado = input().upper()
valor_doce = 2.25
valor_salgado = 4.00
valor_integrais = 6.90

total_doce = 0
total_salgado = 0
total_integrais = 0

i = 0
while i < len(prod_comprado):
	#produto = prod_comprado[i]
		if prod_comprado[i] == "D":
			total_doce += 1
		elif prod_comprado[i] == "S":
			total_salgado += 1
		elif prod_comprado[i] == "I":
			total_integrais += 1
		i += 1
total = sum([valor_doce*total_doce, valor_salgado*total_salgado, valor_integrais*total_integrais])
print(round(total,2))