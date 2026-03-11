from numpy import *

aneis = array(eval(input( "Digite aqui; ")))

i = 0
p = 10000

while i < size (aneis):
	if aneis [i] == 1:
		p *=2
	elif aneis [i] == 3:
		p/=2
	elif aneis [i] == 4:
		p/=4
	i+=1
	
print(p)
	