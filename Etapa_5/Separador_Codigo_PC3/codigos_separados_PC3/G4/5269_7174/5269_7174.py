x=int(input("numero:  "))
cont=0
mult=0
while(x!=0):
	if(x%3==0):
		mult=mult+1
	x=int(input("numero:  "))
	cont=cont+1
por=(mult*100)/cont
print(cont)
print(round(por, 2))