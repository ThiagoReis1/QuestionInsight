
i=0
cont=0

n=int(input("N: "))

while (n!=0 and n>0):
	cont = cont+1

	if (n%2==0):
		i=i+1
	
	n = int(input("N: "))
	
	
p = (i/cont)*100
print(cont)		
print(round(p,2))



		