from numpy import *

v = array(eval(input('Insira as faces do dado tiradas: ')))

i = 0
p = 200.0
while (i < size(v)):
	if (v[i]==1):
		p = p/2
	elif (v[i]==2):
		p = p*3
	elif (v[i]==3):
		p = p/2
	elif (v[i]==4):
		p = p*3
	elif (v[i]==5):
		p = p/2
	elif (v[i]==6):
		p = p*3
	i = i + 1
print(round(p,2))