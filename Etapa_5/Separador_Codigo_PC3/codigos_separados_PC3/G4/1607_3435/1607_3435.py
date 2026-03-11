from numpy import*
from math import *
a = array(eval(input("Quais os andares em q o elevador parou ? (1 a 20) : ")))
i=0
s=0

while(i<size(a)-1):
		d= abs(a[i+1]-a[i])
		d=d*3
		s=s+ d
		i=i+1
		
print(s)