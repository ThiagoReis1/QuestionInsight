from numpy import *
notas=array(eval(input("numeros")))
soma=[0]

for i in range(0,size(notas)):
	if (notas[i]==99):
		notas[i]=(99).replace("0")
		soma=sum(notas)*2
	else:
		soma=sum(notas)
print(soma)