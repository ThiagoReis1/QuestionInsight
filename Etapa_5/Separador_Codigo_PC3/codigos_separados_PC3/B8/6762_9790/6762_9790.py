# faça seu código aqui!
idade = int(input("idade do espectador: "))

if idade < 12:
	valor = 20 + 1.25
	print(round(valor, 2))
elif idade == 12:
	valor = 20 + 2.25
	print(round(valor,2))
elif idade > 12:
	valor = 20 + 3.25
	print(round(valor, 2))