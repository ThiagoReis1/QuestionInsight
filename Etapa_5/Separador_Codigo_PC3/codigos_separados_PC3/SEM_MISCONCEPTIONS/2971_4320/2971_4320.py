juros =  float(input("taxa de juros : "))
valor = float(input("valor apartamento: "))

total = round((1500.00*(1+juros)**36),2)
print(total)

if (valor > total):
	print("nao")
else:
	print("sim")