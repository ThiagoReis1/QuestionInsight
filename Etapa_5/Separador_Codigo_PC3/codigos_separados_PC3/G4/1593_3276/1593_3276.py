from numpy import *

notas = array(eval(input("Notas: ")))

i=0
d=0

while(i<size(notas)):
	notas[i]= (notas[i] * (i +1))
	i=i+1
	d= d+ i
c=sum(notas)/d

print(round(c,2))