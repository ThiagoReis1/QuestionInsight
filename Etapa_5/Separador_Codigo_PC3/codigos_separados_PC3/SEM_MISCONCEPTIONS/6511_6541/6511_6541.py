# faça seu código aqui!
tipo = input()
qt = int(input())

if tipo.upper() == 'B':
	pagar = (qt * 25.90) - ((qt * 25.90) * 0.10)
	
else:
	pagar = qt * 25.90
	
print(round(pagar, 2))