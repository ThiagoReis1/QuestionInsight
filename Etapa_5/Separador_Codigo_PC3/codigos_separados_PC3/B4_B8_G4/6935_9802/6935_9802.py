vt = float(input("valor total da compra: "))
odp = input("opcao de pagamento (D, P ,C)? ")

if odp == "P":
	vf = vt - (0.12 * vt)
	print(round( vf,2 ))
elif odp == "D":
	vf = vt - (0.12 * vt)
	print(round( vf,2 ))
elif odp == "C":
	vf = int(input("quantas vezes: "))
	if vf == 1:
		print(vt)
	else:
		vff = (0.07 * vt) + vt
		print(round(vff,2))

	
	