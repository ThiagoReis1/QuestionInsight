from numpy import*
from numpy.linalg import*
v=array(eval(input("")))
x=min(v)
cp=0
cont=0

while(cp<size(v)):
	if(v[cp]==min(v)):
		cont=cont +1
		print(cp)
	cp=cp+1
