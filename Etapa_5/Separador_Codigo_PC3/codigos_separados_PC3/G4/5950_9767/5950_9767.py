esc = str ( input ("Torta ou Pastel? T/P "))
qtd = int ( input ("Quantidade: "))
qtdc = int ( input ("Quantidade de Cappuccino: "))


if ( esc == "P" ):
	som = ( qtd * 5.00 ) + ( qtdc * 4.50)
	print ( round ( som , 2))
	
else:
	som = ( qtd * 6.00 ) + ( qtdc * 4.50)
	print ( round ( som , 2 ))