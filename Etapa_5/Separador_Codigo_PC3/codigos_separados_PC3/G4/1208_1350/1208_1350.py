from numpy import*
rm= 98.48
dist=array (eval(input("Digite o vetor:")))
i=0
cont=0
while (i<size(dist)):
	if(dist[i]<rm):
		cont=cont+1
	i=i+1
print(rm)
print(cont)