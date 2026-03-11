e = input("Lanche ou Pizza(L/P): ")
q = int(input("Quantidade de lanches ou pizzas: "))
r = int(input("Quantidade de refrigerantes: "))

if e.upper() == 'L':
	pf = (q * 6.00) + (r * 3.00)
else:
	pf = (q * 4.50) + (r * 3.00)

print(round(pf,1))
	