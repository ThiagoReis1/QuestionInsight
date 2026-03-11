abertura = float (input (" valor :"))
fechamento = float ( input (" valor : "))

x = fechamento - abertura

if ( x > 0):
	print("saldo positivo")
	
elif( x == 0):
	print("sem variacao")
	
elif ( x < 0 ):
	print ("saldo negativo")