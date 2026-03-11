esc = input("T ou P: ")
quant = int(input("fatias: "))
caf = int(input("cappuccinos: "))

tor = 6.00
pas = 5.00
cap = 4.50

caff = cap * caff

if(esc == "T"):
	torf = tor * quant
	preco = torf + caff
	print(preco)
	
else:
	pasf = pas * quant
	preco = pastf + caff
	print(preco)