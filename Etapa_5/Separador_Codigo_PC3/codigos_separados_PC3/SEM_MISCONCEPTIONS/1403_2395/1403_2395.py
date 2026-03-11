armadura = input("Nome da armadura: ")
fator = int(input())
if (armadura == "malha"):
	res = (15*fator) - 1
	print(int(res))
else:
	res = (20*fator)- 18
	print(int(res))