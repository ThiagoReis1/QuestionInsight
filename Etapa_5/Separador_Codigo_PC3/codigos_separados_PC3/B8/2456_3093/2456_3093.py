mensal = float(input())
n = int(input())

if (n == 1):
	novo = n * mensal * 0.9
	print(novo)
elif (n == 2):
	novo = n * mensal * 0.7
	print(novo)
elif (n >= 3):
	novo = n * mensal * 0.6
	print(novo)