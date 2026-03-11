try :
	from numpy import *
	a = array(eval(input("Digite as porcentagens de presenca: ")))
	
except NameError :
	print("Digite numeros!")
	
except TypeError :
	print("Cuidado com o que digita!")
	
except SyntaxError :
	print("Digita direito!")
	
else :
	tf = True
	i = 0
	while ( i < size(a) ) :
		if ( a[i] < 0 or a[i] > 100 or a[i] % 1 != 0 ) :
			tf = False
			break
			
		i += 1
		
	if ( tf ) :
		cont = 0
		j = 0
		for i in range(size(a)) :
			if ( a[i] >= 70 ) :
				cont += 1
		print(cont)
		v = zeros(cont, dtype = int)
		for i in range(size(a)) :
			if ( a[i] >= 70 ) :
				v[j] = i
				j += 1
				
		if ( cont > 0 ) :
			print(v)
			
		else :
			print("Kuen kuen kuen...")
	else :
		print("Numeros positivos entre 0 e 100!")