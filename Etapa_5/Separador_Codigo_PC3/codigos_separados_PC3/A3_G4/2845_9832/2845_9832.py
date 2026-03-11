try :
	from numpy import *
	n = array(eval(input("Digite os numeros: ")))
	
except NameError :
	print("Somente numeros!")
	
except TypeError :
	print("Cuidado com os espacos!")
	
except SyntaxError :
	print("Escreve direito!")
	
else :
	i = 0
	tf = True
	while ( i < size(n) ) :
		if ( n[i] < 0 or n[i] > 9) :
			tf = False
			break
			
		i += 1
		
	if ( tf ) :
		for i in range(size(n)) :
			if ( n[i] < 9 ) :
				n[i] += 1
				
			else :
				n[i] = 0
				
		print(n)
	else :
		print("Numeros positivos!")