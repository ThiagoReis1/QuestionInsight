from numpy import *
vet = array(eval(input("Digite: ")))
soma = 0
cont = 0
media = 0
for i in vet:
	if(i > 170):
		soma = soma + i
		cont = cont + 1
		media = soma / cont
if(cont != 0):
	print(round(media,2))
else:
	print(0)



	
	
