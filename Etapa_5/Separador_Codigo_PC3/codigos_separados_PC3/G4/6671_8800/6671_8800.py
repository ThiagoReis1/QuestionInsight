from numpy import*

vet = array(eval(input("digite: ")))

cont = 0
soma = 0
for i in vet:
	if i > 15:
		cont = cont + 1
		soma = soma + i
if cont > 0:
	media = round((soma/cont), 2)
	print(media)
else:
	print(0.0)
