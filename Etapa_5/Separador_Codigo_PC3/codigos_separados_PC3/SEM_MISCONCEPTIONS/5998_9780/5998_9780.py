quant_macas = int(input("Insira a quantidade de macas: "))

if quant_macas < 12 :
	total = quant_macas * 0.30

else:
	total = quant_macas * 0.25
	
print(round(total, 2))
	