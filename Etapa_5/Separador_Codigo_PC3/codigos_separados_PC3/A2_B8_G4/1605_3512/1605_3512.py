from numpy import*

vtr= array(eval(input("Vasco eh ruim: ")))
cont=0
soma=200

while(cont<size(vtr)):

	if vtr[cont]==1:
		soma=soma * 4
	elif vtr[cont] == 2:
		soma=soma * 2
	elif vtr[cont]==3:
		soma=soma
	elif vtr[cont]==4:
		soma=soma/2	
	cont= cont + 1
	
print(round(soma,2))