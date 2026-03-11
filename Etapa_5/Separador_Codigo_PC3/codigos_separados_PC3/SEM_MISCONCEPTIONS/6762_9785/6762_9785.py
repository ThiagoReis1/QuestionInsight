# faça seu código aqui!
idade = float(input())
if idade < 12:
	valor = 1.25 + 20
	
elif idade == 12:
	valor = 2.25 + 20
else:
	valor = 3.25 + 20
	
print(round(valor, 2))