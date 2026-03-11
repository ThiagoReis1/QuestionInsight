m = float(input("quant inicial de massa: "))
a = int(input("quant de anos: "))
cont = 0
while cont!=a:
	m = m-(0.05*m)
	cont = cont+1
	print(round(m,2))