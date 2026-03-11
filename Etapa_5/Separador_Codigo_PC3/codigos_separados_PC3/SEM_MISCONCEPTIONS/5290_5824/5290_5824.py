dado=int(input("Lancamento:"))
cont=0
faces=0
while dado!=-1:
	cont=cont+1
	if dado==5:
		faces=faces+1
		
	dado=int(input("Lancamento:"))
print(cont)
print(round(100*faces/cont,2))
	

