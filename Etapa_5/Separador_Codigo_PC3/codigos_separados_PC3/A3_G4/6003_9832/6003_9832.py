c = input("Quantidade de cenouras: ")

try :
	c = int(c)
	
except ValueError:
	print("Digite valores positivos!")
	
else :
	if ( c < 0 ) :
		print("Digite valores positivos!")
		
	else :
		t = 0
		if (  c < 5 ) :
			t = c * 1.2
			print( round(t,2) )
		
		else :
			t = c * 0.9
			print( round(t,2) )