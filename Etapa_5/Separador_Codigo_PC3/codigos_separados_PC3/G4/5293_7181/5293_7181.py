n=int(input("numero:  "))
par=0 
cont=0
while(n!=0):
	if(n%2==0):
		par=par+1
	n=int(input("numero:  "))
	cont=cont+1

por=par*100/cont
print(cont)
print(round(por, 2))