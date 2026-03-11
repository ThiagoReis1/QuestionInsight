vc = float(input("valor jovi: "))
vid = float(input("valor jovi: "))
dfm = float(input("valor jovi: "))
tax = float(input("juros: "))

tx = tax / 100
mes = 0

if((vc <= 0) or (vid <= 0) or (dfm <= 0) or (tx <= 0)):
	print("Dados incorretos")
else:
	while(vid < vc):
		vid = round((vid * tx) + dfm + vid, 2)
		mes = mes + 1
		
	print(mes)