x = input("Digite um numero: ")

try :
	x = float(x)
	
except ValueError :
	print("Digite numeros!")
	
else :
	x1 = 0
	if ( x % 43 == 0 ) :
		x1 = x / 43
		print( int(x1) )
		print("sim")
	
	else :
		x1 = x % 43
		print( int(x1) )
		print("nao")