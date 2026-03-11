x=float(input("Numero real: "))
k=int(input("Quantidade de termos: "))
cont=1
s=0

while cont<=k:
	s=s+(cont/x)
	cont=cont+1
	
print(round(s,10))
	
	
	