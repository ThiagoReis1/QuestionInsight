cons = float(input("COnsumo:  "))
taxa = (cons+30)
if cons<10:
	tarif = (cons*3)+30
	print(round(tarif, 2))
else:
	tarif = (cons*3.5)+30
	print(round(tarif, 2))