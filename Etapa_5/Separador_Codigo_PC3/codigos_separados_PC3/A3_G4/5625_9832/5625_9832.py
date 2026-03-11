o = input("Tapioca (t ou T) ou Salgado (s ou S)? ").upper()

if ( o != "T" and o != "S" ) :
	print("T ou S!")
	
else:
	q1 = input("Quantitade de alimentos: ")
	q2 = input("Quantidade de acais: ")
	
	try :
		q1 = int(q1)
		q2 = int(q2)
		
	except ValueError :
		print("Digite numeros!")
		
	else:
		if ( q1 < 0 or q2 < 0 ) :
			print("Digite valores positivos!")
			
		else :
			t = 5.5
			s = 4.0
			a = 10.0
			a = a * q2
			total = 0
			if ( o == "S" ) :
				total = ( q1 * s ) + a
				print( round(total,2) )
				
			else:
				total = ( q1 * t ) + a
				print( round(total,2) )