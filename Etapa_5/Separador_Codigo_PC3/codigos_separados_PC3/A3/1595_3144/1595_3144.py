from numpy import*
from numpy.linalg import*

n = array(eval(input("notas dos trabalhos:")))

menor=999999999999999999999999
indice=0
for i in range(n):
	if shape(n)< menor:
		indice = i+1
		menor = n[i]
	else:
		i = i+1
x=sum(n)/size(n)
print(x)

