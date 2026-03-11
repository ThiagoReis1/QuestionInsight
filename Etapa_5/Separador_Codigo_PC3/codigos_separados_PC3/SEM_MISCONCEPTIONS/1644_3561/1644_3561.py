from  numpy import *
notas=array(eval(input("notas:")))  
reprovados=0
for i in range(size(notas)):
	if(notas[i]<5):
	   reprovados= reprovados+1
print(reprovados)
j=0
vet2= zeros(reprovados, dtype=int)
for i in range(size(notas)):
	if(notas[i]<5):
		vet2[j]=i
		j=j+1
print(vet2)