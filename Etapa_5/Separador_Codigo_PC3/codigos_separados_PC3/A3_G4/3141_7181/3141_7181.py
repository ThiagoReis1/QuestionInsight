from numpy import *

v=array(eval(input("numeros:  ")))
m=0.0
sv=0
ps=0
for i in range(0, size(v)):
	m=m+(v[i-1]**(1/6))
	
sv=m/(size(v))
ps=sv**6
print(round(ps, 2))