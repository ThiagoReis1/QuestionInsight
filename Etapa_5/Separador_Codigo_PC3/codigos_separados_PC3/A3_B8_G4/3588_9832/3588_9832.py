from numpy import *

try :
	a = array(eval(input("Digite a ordem dos aneis acertados: ")))
	
except NameError :
	print("Numeros!!!")
	
else :
	tf = True
	i = 0
	t = 10000
	while ( i < size(a) ) :
		if ( a[i] > 4 or a[i] < 1 ) :
			tf = False
			break
		elif ( a[i] == 1 ) :
			t *= 2
		elif ( a[i] == 3 ) :
			t /= 2
		elif ( a[i] == 4) :
			t /= 4
		i += 1
		
	if ( tf == True ) :
		print(round(t,2))
		
	else :
		print("Bobo.")