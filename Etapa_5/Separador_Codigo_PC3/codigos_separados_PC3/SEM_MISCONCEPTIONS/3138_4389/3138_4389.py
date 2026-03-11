from numpy import*
v = array(eval(input("Informe os termos do vetor: \n")))
cont = 0
soma = 0
while (cont<size(v)):
	soma = soma + (v[cont])**7
	cont = cont + 1
media = soma/size(v)
resultado = media**(1/7)
print(round(resultado,2))


	
