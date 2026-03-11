# faça seu código aqui!
peso=float(input())
fixo=10
if peso<5:
	total=fixo+3.75
elif peso==5:
	total=fixo+4.75
elif peso>5:
	total=fixo+5.75
print(round(total, 2))