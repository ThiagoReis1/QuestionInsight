from numpy import*
v=array(eval(input("digite o vetor")))
cont=0
maior=0
for i in range(size(v)):
	if(v[i]>v[0]):
		cont=cont+1
		maior=v[i]
	if(maior<v[i]):
		maior=v[i]
		cont=cont+1
print(maior)
print(cont)