compra = float(input("total comp"))
codpg = input("cod opcao pg (D ,P ou C)")
if codpg == "D" or codpg == "P":
	valor = compra*0.81
elif codpg == "C":
	vezes = int(input())
	if vezes == 1:
		valor = compra
	elif vezes == 2:
		valor = compra*1.09
else:
	print()
	exit()
print(round(valor,2))