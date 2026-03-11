velocidade = int(input("digite a velocidade que voce quer: "))

if velocidade < 50:
	total = 60.00 + 4.50
elif velocidade == 50:
	total = 60.00 + 5.50
else:
	total = 60.00 + 6.50
print(round(total, 2))