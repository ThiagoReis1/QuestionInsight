quantidade = float(input("Quantidade de pecas: "))

if(quantidade < 10):
	total = 30 + 3.25
elif(quantidade == 10):
	total = 30 + 4.50
elif(quantidade > 10):
	total = 30+ 6.00
print("total= ", total)