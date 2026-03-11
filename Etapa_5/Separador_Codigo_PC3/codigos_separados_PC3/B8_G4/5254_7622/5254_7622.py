p = float(input("preco do produto: "))
c = int(input("codigo da regiao: "))

if c == 1:
	f = 10
	venda = (p - (p * 0.4)) + p * (f/100)
elif c == 2:
	f = 8
	venda = (p - p * 0.4) + p * (f/100)
elif c == 3:
	venda = (p - p * 0.4)
elif c == 4:
	f = 2
	venda = (p - p * 0.4) + p * (f/100)
	
print(round(venda,2))	
	