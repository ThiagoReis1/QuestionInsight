from numpy import *

tiro= array(eval(input()))

i=0
acum=10000
while i < size(tiro):
	if tiro[i]==1:
		acum=acum*2
	elif tiro[i]==2:
		acum=acum
	elif tiro[i]==3:
		acum=acum/2
	elif tiro[i]==4:
		acum=acum/4
	i+=1
print(round(acum,2))