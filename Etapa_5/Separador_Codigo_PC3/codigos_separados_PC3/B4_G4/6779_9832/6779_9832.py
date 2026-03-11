b = 18
j = 16
d = 2023

i = input("Digite o ano de nascimento: ")
p = input("Digite o pais escolhido (J ou B): ").upper()

try :
	i = int(i)
	
except ValueError :
	print("invalido")
	
else :
	if ( i < 1900 ) :
		print("invalido")
		
	elif ( p != "B" and p != "J" ) :
		print("invalido")
		
	elif ( p == "B" ) :
		if ( d - i < b ) :
			print("nao")
			b = b - (d - i)
			print(b)
			
		else :
			print("sim")
			b = ( d - i ) - b
			print(b)
	else :
		if ( d - i < j ) :
			print("nao")
			j = j - ( d -i )
			print(j)
			
		else :
			print("sim")
			j = ( d - i ) - j
			print(j)