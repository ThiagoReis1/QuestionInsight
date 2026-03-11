from numpy import *

anel = array(eval(input("Acertos: ")))

i = 0
pt = 0

while i < size(anel):
	if anel[i] == 1:
		pt += 100
	elif anel[i] == 2:
		pt += 60
	elif anel[i] == 3:
		pt += 20
	i += 1
	
print(round(pt,2))