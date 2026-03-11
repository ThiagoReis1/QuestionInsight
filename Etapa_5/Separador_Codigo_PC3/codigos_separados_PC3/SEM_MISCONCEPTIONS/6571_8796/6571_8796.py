# faça seu código aqui!
peso = float(input())
valor_fixo = 10

if peso < 5:
	total = valor_fixo + 3.75
elif peso == 5:
	total = valor_fixo + 4.75
else:
	total = valor_fixo + 5.75
print('total=',round(total, 2))