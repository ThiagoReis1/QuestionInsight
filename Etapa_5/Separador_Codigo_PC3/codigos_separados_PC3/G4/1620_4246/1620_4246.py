from numpy import *

tempo = array(eval(input()))
perc = array(eval(input()))

cont = 0
a = size(perc)
l = 0

while cont < a:
	l = l + 5*tempo[cont]*perc[cont]/100
	cont = cont +  1
fin = round(l ,2)
print(fin)