cacho=4.25
desconto=5.0
qtd=float(input("insira a quantidade:"))

if qtd >=3:
	print(cacho*qtd)
if qtd < 3:
	print(desconto*qtd)