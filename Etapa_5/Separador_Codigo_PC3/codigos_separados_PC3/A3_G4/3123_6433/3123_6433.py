from numpy import *
from math import *

n = array(eval(input("numeros reais positivos: ")))

m = 0
p = 0
i = 0
while i<size(n):
	
	p += pow(n[i], -1)
	m = pow(p/size(n), -1)
	i = i + 1
	
print(round(m,2))