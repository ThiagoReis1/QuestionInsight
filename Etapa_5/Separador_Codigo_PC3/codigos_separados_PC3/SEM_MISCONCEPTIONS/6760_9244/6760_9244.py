quant_pecas = int(input("digite a quantidade de pecas de roupa para lavagem: "))

fixo = 30.0

if (quant_pecas <10):
	custo = fixo + 3.25
elif (quant_pecas == 10):
	custo = fixo + 4.50
else:
	custo = fixo + 6.00
print(custo)