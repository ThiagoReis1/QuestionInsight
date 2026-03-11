Vt = float(input("Digite o valor total da compra: "))
Op = input("Digite a opcao de pagamento: ").upper()

if Op == "D":
	Vf = Vt - Vt * 0.19
	print(round(Vf,2))
elif Op == "P":
	Vf = Vt - Vt * 0.19
	print(round(Vf,2))
elif Op == "C":
	Qp = input("deseja pagar quantas vezes? ")
	if Qp == "1":
		Vf = Vt
		print(round(Vf,2))
	elif Qp == "2":
		Vf = Vt + Vt * 0.09
		print(round(Vf,2))