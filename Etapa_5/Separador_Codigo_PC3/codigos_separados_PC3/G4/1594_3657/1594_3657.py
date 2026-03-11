from numpy import*
dano= array(eval(input("De o vetor de danos: ")))
i=0
n=size(dano)
while(i<n ):
	if(i==0):
		total=dano[i]
	else:
		total=total+(i+1)*dano[i]
	i=i+1
print(total)
