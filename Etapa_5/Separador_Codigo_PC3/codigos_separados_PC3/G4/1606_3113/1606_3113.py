from numpy import*

na = array(eval(input("andares caminhados:")))

i = 0 # vari. conta.
ii = i + 1
d = 0 #distancia

while(i < size(na)):
	b = na[ii] - na[i]
	d = d + b
	i = i + 1
print(d)
	
	
