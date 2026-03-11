item = input("Coxinha ou Esfirra: ").upper()
qce = float(input("Quantidade de coxinha ou Esfirra: "))
qs = float(input("Quantidade de Suco: "))

c = 2
e = 4.50
s = 6
vc = (qce * c) + (qs * s)
ve = (qce * e) + (qs * s)

if(item == "C"):
	print(round(vc,2))

else:
	print(round(ve,2))