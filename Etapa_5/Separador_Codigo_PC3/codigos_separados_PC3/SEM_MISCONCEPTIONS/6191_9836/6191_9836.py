caouco=input('lancamento:').upper()

qtcara=0

while caouco != 'S':
	if caouco == "CARA":
		qtcara += 1 
	caouco = input('prox lancamento:').upper()
	
print(qtcara)	

	