from numpy import*
v = array(eval(input("Digite: ")))
cont = 0
soma = 0
while(cont<size(v) and soma != 4):
	if(v[cont]==1):
		soma=soma+80
	elif(v[cont]==2):
		soma = soma + 40
	elif(v[cont]==3):
		soma = soma + 20
	elif(v[cont]==4):
		soma = soma + 10
	cont = cont + 1
print(soma)
		