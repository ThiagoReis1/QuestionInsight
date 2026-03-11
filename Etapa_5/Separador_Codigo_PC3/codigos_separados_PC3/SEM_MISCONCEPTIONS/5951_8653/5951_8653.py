tipo = input()
if tipo == "T":
	quantidadeT = int(input())
	quantidadeA = int(input())
	print(round((quantidadeT * 4.50 + quantidadeA * 12), 2))
else:
	quantidadeS = int(input())
	quantidadeA = int(input())
	print(round((quantidadeS * 5 + quantidadeA * 12), 2))