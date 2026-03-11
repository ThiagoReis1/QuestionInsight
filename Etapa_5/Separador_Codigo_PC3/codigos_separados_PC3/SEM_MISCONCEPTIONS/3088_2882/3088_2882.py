n=int(input("Numero: "))

i=0
cont1=0
cont2=0
while(n != 0):
	n=int(input("Numero: "))
	if(n%2==0):
		cont1=cont1+1
	else:
		cont2=cont2+1
	i=i+1
		
if(i>0):
	print(round((cont1/i)*100),2)
	print(round((cont2/i)*100),2)