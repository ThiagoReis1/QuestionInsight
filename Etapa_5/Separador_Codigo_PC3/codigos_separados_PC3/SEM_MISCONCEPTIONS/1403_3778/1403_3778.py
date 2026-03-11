armadura = input()
fator = int(input())

if armadura == "malha":
	res = 15 * fator - 1
	print(round(res, 2))
else:
	res = 20 * fator - 18
	print(round(res, 2))