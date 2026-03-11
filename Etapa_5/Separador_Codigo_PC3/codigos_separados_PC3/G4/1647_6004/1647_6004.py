from numpy import *

af = array(eval(input("aulas frequentadas: ")))
a=0

for i in range(size(af)):
	if (af[i]>=0.70):
		a[i] = a[i]+1