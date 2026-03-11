valor = float(input())
codigo = input()

if codigo == 'C':
	cartao = int(input())
	if cartao == 1:
		total = valor
	else:
		total = valor + 6*valor/100
else: 
	total = valor - valor*11/100
	
print(round(total, 2))