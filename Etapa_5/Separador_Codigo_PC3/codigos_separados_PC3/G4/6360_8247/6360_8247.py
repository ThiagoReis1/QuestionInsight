num = int(input())

for i in range(num, 0, -4):
	print(num)
	num = num - 4
	if num == 0:
		print("0")
		print("Fim da contagem regressiva!")
		break
	if num < 0:
		print("Fim da contagem regressiva!")