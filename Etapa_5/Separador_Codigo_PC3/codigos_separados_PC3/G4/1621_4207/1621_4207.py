from numpy import *

p = array(input(""))
qnt= array(eval(input("")))

x= zeros(size(p), dtype=int)

for i in range(size(p)):
	if(p[i]=='ARROZ' and qnt[i]==p[i]):
		x[0]= qnt[i]*1.25
	