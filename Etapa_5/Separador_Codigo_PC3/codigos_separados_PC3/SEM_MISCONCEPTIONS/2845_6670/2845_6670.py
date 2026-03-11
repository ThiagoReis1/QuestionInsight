from numpy import *

codigo=array(eval(input()))

#num=array([0,1,2,3,4,5,6,7,8,9])

for i in range(size(codigo)):
	if codigo[i]==9:
		codigo[i]=-1
	codigo[i]=codigo[i]+1

print(codigo)