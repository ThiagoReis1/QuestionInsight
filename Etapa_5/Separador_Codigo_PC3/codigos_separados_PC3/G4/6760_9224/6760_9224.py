# faça seu código aqui!
qtd = int(input("digite a quantidade de pecas:"))

if qtd < 10:
	v = 3.25 + 30.00
	
elif qtd == 10:
	v = 4.50 + 30.00

else:
	v = 6.00 + 30.00
	
print(round(v, 2))