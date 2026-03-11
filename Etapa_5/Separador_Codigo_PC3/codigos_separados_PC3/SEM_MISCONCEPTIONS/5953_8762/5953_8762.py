tipo = input("Informe(L/P): ")
quant = int(input("Informe a quantidade: "))
ref = int(input("Quantidade de refrigerantes: "))

tp = tipo.upper()
if tp=='L':
	total = (quant*6.00)+(ref*3.00)
	print(total)
else: 
	total = (quant*13.50)+(ref*3.00)
	print(total)