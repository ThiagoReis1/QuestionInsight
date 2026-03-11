num=int(input("le"))
cont=1
cont2=1
i=0
x=num
media=num/cont
while(num!=0):
	num=int(input("le"))
	if((num%2==0)):
		mediap=num+x/cont
	else:
		mediai=num+x/cont2
	cont=cont+1
	cont2=cont2+1
	i=i+1
print(round(mediap,2))
print(round(mediai,2))
		