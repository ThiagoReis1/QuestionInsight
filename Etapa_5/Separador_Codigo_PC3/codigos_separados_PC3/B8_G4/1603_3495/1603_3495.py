from numpy import*

v=array(eval(input()))
cont=0
soma=0

while (v[cont]<4):
	if v[cont]==1:
		soma=soma+80
		cont=cont+1
	elif v[cont]==2:
		soma=soma+40
		cont=cont+1
	elif v[cont]==3:
		soma=soma+20
		cont=cont+1

print(soma)