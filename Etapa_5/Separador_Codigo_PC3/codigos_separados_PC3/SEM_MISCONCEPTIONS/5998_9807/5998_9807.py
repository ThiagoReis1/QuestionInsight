quant = int(input("Digite a quantidade de macas: "))
a = quant * 0.30
b = quant * 0.25
if quant < 12:
	print(round(a,2))
else: 
	print(round(b,2))