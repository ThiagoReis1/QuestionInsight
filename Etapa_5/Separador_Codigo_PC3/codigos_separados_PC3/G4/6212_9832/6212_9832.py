c = 0
n = 0
while ( n != -1 ) :
	if ( n > 25 and n < 86 ) :
		c += 1
	n = input("Digite um numero: ")
	try :
		n = int(n)
		
	except ValueError :
		print("Bah")
		n = -1
	
print(c)