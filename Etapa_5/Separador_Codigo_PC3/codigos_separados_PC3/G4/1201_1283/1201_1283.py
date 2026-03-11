from numpy import*

r=array(eval(input("Digite aqui: ")))
i=0
cont=0
while(i<size(r)):
	if(r[i]>=0 and r[i]<40):
		cont=cont+1
	i=i+1
mai=array(zeros(cont,dtype=float))
i=0
j=0
while(i<size(r)):
	if(r[i]>=0 and r[i]<40):
		mai[j]=r[i]
		j=j+1
	i=i+1
print(mai)