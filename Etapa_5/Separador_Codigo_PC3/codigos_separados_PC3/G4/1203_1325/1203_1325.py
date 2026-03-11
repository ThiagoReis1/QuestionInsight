from numpy import*
rm = 2.5
salto = array (eval(input()))
i = 0
cont = 0
while ( i<size(salto)):
	if (salto[i]>rm):
		cont = cont + 1
	i = i+1
print (rm)
print (cont)