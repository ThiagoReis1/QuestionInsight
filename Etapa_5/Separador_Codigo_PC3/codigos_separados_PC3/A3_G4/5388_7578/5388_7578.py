from numpy import *

c=array(eval(input("codigo criado").upper()))
i=0
p=0

while i>size(c):
	if c==("A","E","I","O","U"):
		p=25.12*c
	else:
		40.12*c
	
print(sum(c))