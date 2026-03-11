from numpy import*
from numpy.linalg import*
n=array(eval(input("")))
lin=shape(n)[0]
col=shape(n)[1]
menor=99999999999
indice=0
v=zeros(lin)
for i in range(lin):
	for j in range(col):
		if n[i,j]< menor:
			indice=i
			menor=n[i,j]
		else:
			j=j-1
print(indice)