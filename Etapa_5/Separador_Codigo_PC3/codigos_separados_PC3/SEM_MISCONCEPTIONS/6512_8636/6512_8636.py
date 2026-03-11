# faça seu código aqui!
dd = int(input("quantidade de duplas deliciosas: "))

total = 32.90 * dd
desconto = total - total* 0.20

if (dd > 3):
	print(round(desconto, 2))
	
else:
	print(round(total, 2))