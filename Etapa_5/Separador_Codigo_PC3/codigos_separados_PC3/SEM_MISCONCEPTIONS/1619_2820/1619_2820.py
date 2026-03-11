from numpy import *
x = array(eval (input ("")))
y = array(eval (input ("")))

z = arange(size(x))

QUENTE = 90

MORNO = 45

FRIO = 0

i = 0

while(i < size(x)):
    if(x[i] == "QUENTE"):
        	z[i] = y[i] * QUENTE
   	elif([i] == "MORNO"):
       	z[i] = y[i] * MORNO
    	else([i] == "MORNO"):
       	 z[i] = y[i] * FRIO
   		 i += 1

P = sum(z)
print(round(P, 2))