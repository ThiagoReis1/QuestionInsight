from numpy import *
notas = array(eval(input("media final: ")))
cont=0
for i in range(size(notas)):
	if notas[i]>=70:
		cont=cont+1
print(cont)
result=zeros(cont,dtype=int)
c=0
for j in range(size(notas)):
	if notas[j]>=70:
		result[c]=j
		c=c+1
print(result)
