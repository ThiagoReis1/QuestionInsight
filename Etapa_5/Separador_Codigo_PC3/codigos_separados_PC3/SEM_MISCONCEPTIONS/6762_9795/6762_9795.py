# faça seu código aqui!

idade = int(input("idade: "))

if idade < 12:
	ingresso = 20 + 1.25
	print(round(ingresso, 2))
elif idade == 12:
	ingresso = 20 + 2.25
	print(round(ingresso, 2))
else:
	ingresso = 20 + 3.25
	print(round(ingresso, 2))