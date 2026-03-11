p = input("Digite sua pontuacao: ")

try :
	p = float(p)
	
except ValueError :
	print("Dados invalidos.")
	
else :
	if ( p < 0 ) :
		print("Dados invalidos.")
		
	elif ( p == 100 ) :
		print("limite")
		
	elif ( p > 100 ) :
		print("maior")
		
	elif ( p < 100 ) :
		print("menor")