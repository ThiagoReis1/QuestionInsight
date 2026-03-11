idade = int(input("digite a idade do espectador: "))
if idade < 12:
	total = 1.25 + 20
	print(total)
elif idade == 12:
	total = 2.25 + 20
	print(total)
elif idade > 12:
	total = 3.25 + 20
	print(total)
	