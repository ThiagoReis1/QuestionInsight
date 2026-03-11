from numpy import *

try :
	n = array(eval(input("Digite as tres notas: ")))
	
except NameError :
	print("Tres notas!!!")
	
else :
	if ( size(n) == 3 ) :
		tf = True
		i = 0
		t = 0
		while (i < size(n)) :
			if (n[i] < 0 or n[i] > 10) :
				tf = False
				break
			t += n[i]*(i+1)
			i += 1
		
		if ( tf == True ) :
			t = t/6
			print(round(t,2))
		else :
			print("Bobo.")
	else :
		print("Bobao.")