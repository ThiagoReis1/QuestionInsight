# faça seu código aqui!

ingresso = 20
idade = int(input("por: "))

if idade > 12:
	total = ingresso + 3.25
elif idade == 12:
	total = ingresso + 2.25
else:
	total = ingresso + 1.25
print(round(total, 2))