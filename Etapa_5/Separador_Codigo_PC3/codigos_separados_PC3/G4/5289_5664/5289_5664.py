f=int(input('face: '))

cont=0
i=0
while f!=-1 or 0<f<7:
	if f==6:
		i=i+1
	cont=cont+1
	f=int(input('face: '))
print(cont)
print(round(i*100/cont,2))
	
	