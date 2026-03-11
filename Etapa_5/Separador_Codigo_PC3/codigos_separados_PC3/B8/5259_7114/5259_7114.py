mens = float(input("Digite o valor da mensalidade: "))
num = int(input("Digite o numero de criancas: "))

if (num == 1):
	total = (mens * num) - (mens * num * 0.10)
	print(round(total, 2))
elif (num == 2):
	total2 = (mens * num) - (mens * num * 0.30)
	print(round(total2, 2))
elif (num >= 3):
	total3 = (mens * num) - (mens * num * 0.40)
	print(round(total3, 2))