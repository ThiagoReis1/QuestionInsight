a = input("B para bolo ou C para croissant: ").upper()
q = int(input("quantidade: "))
qcappuccinos = int(input("quantidade: "))

if(a == "B"):
	 total = (3*q)+(5.50*qcappuccinos)
else:
	total = (6*q)+(5.50*qcappuccinos)
print(total)