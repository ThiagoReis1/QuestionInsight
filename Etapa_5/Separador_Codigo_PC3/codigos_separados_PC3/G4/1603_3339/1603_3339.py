from numpy import *

v = array(eval(input("aneis acertados")))

i = 0
a = 0

while( i < size(v) - 1 and v[i] < 4 ):
	if(v[i] == 1 ):
		a = a + 80
	elif(v[i] == 2 ):
		a = a + 40
	else:
		a = a + 20
	i = i + 1
print(a)
		
	

