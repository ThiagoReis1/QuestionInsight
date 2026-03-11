ce = input("digite c ou e: ").upper()
qnt_ce = int(input("digite a quantidade de esfirras ou coxinhas: "))
qnt_suco = int(input("digite a quantidade de sucos: "))
if ce == "C":
	print((qnt_ce * 2) + (qnt_suco * 6))
else:
	print((qnt_ce * 4.5) + (qnt_suco * 6))
