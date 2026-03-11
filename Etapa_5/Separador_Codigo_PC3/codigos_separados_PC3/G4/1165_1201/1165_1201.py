n=int(input())
cont=1
Sb= (1/6)
while(cont<n):
	Sb= Sb + (-1)**(cont)*((cont+1)**3)/(5+(2*cont+1))
	cont=cont+1
print(round(Sb,9))