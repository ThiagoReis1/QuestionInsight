numin= int(input("numero de bacteria:"))
hora = int(input("hora:"))
soma = numin
conth = 0 
while(conth<hora):
	cres = int(soma * (15/100))
	soma = soma + cres
	conth = conth + 1
	print(soma)
