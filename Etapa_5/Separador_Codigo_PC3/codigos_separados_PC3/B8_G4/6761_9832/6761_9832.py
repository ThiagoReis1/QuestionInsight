ab = 60.00

vi = input("Digite a velocidade da internet: ")

try :
	vi = float(vi)
	
except ValueError :
	print("Dados invalidos.")
	
else :
	if ( vi <= 0 ) :
		print("Dados invalidos.")
		
	elif ( vi == 50 ) :
		ab = ab + 5.5
		print(round(ab,2))
		
	elif ( vi < 50 ) :
		ab = ab + 4.5
		print(round(ab,2))
		
	elif ( vi > 50 ) :
		ab = ab + 6.5
		print(round(ab,2))