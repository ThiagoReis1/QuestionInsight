# faça seu código aqui!
peso = float(input("peso em kg:"))
precofixo = 10

if peso < 5:
 total = 3.75 + precofixo
elif peso == 5:
 total = 4.75 + precofixo
else:
 total = 5.75 + precofixo

print(round(total, 2))
	