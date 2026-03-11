x=input("Nome do aminoacido: ".lower())

o= 15.9994
c= 12.011
n= 14.0067
s= 32.066
h= 1.00794

print("Entrada: ", x.lower())

cis= ((3*c) + (7*h) + (n) + (2*o) + (s))
iso= ((6*c) + (13*h) + (n) + (2*o))
met= ((5*c) + (11*h) + (n) + (2*o) + (s))

if(x.lower=="cisteina" or x.lower()=="isoleucina" or x.lower()=="metionina"):
	if(x.lower=="cisteina"):
		print(round(cis, 2)
	elif(x.lower=="isoleucina"):
		print(round(iso, 2)
	else:
		print(round(met, 2)
else:
	print("Dado invalido")