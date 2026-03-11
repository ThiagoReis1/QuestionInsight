bs=input("Bolo ou salgado?:(B/S)")
qte=int(input("quantidade de fatias ou salgados:"))
qtec=int(input("Quantidade de capuccinos:"))
if (bs.upper()=="B"):
	total=(qte*5)+(qtec*7.5)
	print(float(round(total,1)))
if (bs.upper()=="S"):
	total=(qte*4)+(qtec*7.5)
	print(float(round(total,1)))