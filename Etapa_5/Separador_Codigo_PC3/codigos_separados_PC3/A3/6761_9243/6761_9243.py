velocidade = int(input("Digite a velocidade: "))
velocidade = 60.00
if velocidade < 50:
	print(round(50 + 4.50))
elif velocidade == 50:
	print(round(50 + 5.50))
else:
	print(round(50 + 6.50))

