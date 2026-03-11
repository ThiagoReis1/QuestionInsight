quant = int(input("digite a quantidade de cenouras:"))
a = quant * 1.20
b = quant * 0.90

if quant >= 5:
	print(round(b, 2))
else:
	print(round(a, 2))