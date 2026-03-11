p = float(input("preco do produto: "))
c = int(input("codigo da regiao: "))

if (c == 1):
	frete = 10/100*p
elif (c == 2):
	frete = 8/100*p
elif (c == 4):
	frete = 2/100*p
else:
	frete = 0
	
valor_da_venda = (p-p*40//100)+ p*(frete/100)

print(round(valor_da_venda,2))