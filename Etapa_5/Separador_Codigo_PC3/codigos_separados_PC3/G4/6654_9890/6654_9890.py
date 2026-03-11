from numpy import *
vet=array(eval(input("SUAS NOTAS: ")))
peso=array([1,3,2,5])
i=0
soma=0
while i<size(vet):
	soma=soma+vet[i]*peso[i]
	i=i+1
media=soma/ sum (peso)
print(round(media,2))
	