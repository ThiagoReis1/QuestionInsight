idade = int(input())
ingresso = 20.00
if idade < 12:
	ingresso = ingresso + 1.25
	print(round(ingresso,2))
elif idade == 12:
	ingresso = ingresso + 2.25
	print(round(ingresso,2))
else:
	ingresso = ingresso + 3.25
	print(round(ingresso,2))