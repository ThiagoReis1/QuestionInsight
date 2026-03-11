from  numpy import*
v=array(eval(input("vetor: ")))
peso=[2,1,5]
i=0
cont=0
soma=0

while i < size(v):
	cont=cont+v[i]*peso[i]
	
	i=i+1
soma=sum(peso)
media= cont/soma
print(round(media,2))