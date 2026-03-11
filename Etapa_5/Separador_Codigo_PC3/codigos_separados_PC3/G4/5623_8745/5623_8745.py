bos = input("bolo ou salgado(B/S): ")
qbs = int(input("quantidade de fatias de bolo ou salgados: "))
qc = int(input("quantidade de cappuccinos: "))
if (bos == "B"):
	vt = (qbs*5)+(qc*7.50)
	print(vt)
else:
	vt = (qbs*4)+(qc*7.50)
	print(vt)