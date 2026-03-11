#numero de jogadas dado

dado = int(input("Digite o valor: "))
dado = 1
total = 0
fim = 6

if (dado == "6"):
	print(total)
else:
	while (dado < 6):
	dado = dado + 1
	total = total + 1 
	print(total)