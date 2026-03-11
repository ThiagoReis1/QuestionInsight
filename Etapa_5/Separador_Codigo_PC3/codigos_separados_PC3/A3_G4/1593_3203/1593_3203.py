from numpy import*
from numpy.linalg import*

n = array(eval(input('')))

soma=0
peso=1
cont=0
contp=0

for x in range(size(n)):
	soma=n[x]*peso
	peso=peso+1
	cont=cont+soma
	contp=contp+peso-1

a=cont/contp
print(round(a, 2))
