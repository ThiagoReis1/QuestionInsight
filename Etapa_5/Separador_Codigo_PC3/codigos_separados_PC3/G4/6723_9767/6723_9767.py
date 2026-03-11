#variaveis
x = int ( input ("Insira o numero: "))
div = x % 19

#corpo
if ( div == 0):
	qd = ( x // 19 )
	print ( qd )
	print ( "sim" )
	
else: 
	qd = ( x % 19 )
	print ( qd )
	print ( "nao")
	
