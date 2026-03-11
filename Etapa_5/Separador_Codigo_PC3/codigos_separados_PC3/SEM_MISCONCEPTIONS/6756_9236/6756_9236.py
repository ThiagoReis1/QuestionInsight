hospedagem = int(input("digite os dias de hospedagem: "))
diaria = 175

if (hospedagem < 15):
	total = diaria * hospedagem + 20
elif (hospedagem == 15):
	total = diaria * hospedagem + 16
else:
	total = diaria * hospedagem + 10
print(total)