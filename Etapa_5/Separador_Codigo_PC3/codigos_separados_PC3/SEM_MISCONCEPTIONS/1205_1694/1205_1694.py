from numpy import*

salto=array(eval(input("Distancias:")))
recorde=8.95
i=0
c=0

while i<size(salto):
	if salto[i]>recorde:
		c=c+1
		
	i=i+1
print	(recorde)
print (c)