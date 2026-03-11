conta = float(input("digite o valor do consumo: "))

if conta <= 300:
	total = conta + conta*0.1
	print(round(total,2))
if conta > 300:
	total = conta + conta*0.06
	print(round(total,2))