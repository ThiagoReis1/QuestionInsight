cm = input("\"T\" para Tapioca e \"S\" para Salgado: ")
qnt = int(input("Digite a quantidade: "))
ac = int(input("Digite a quantidade de acais: "))

if cm.upper() == "T":
	vlr = qnt * 4.5 + ac * 12.0
	print(round(vlr, 2))
if cm.upper() == "S":
	vlr =  qnt * 5.0 + ac * 12.0
	print(round(vlr, 2))