num = int(input())

cont = 0

for i in range(num, -2, -2):
	if i >= 0:
		print(i)
	if i <= 0:
		print("Fim da contagem regressiva!")