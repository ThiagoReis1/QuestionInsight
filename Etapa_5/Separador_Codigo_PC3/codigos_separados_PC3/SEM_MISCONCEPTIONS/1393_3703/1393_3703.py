peso = float(input())
if 0 < peso < 4999.9:
	frete = peso*0.05
	print(round(frete,2))
else:
	frete = peso*0.04 + 60
	print(round(frete,2))