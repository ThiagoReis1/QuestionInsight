# faça seu código aqui!
diarias = 100
quant_de_dias = int(input("digite um numero"))

if quant_de_dias <7:
	add = 15
elif quant_de_dias == 7:
	add = 12 
else:
	quant_de_dias >10
	add = 10
	
total = (diarias * quant_de_dias) + add

print(round(total,2))