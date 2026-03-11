from numpy import*
vet=array(eval(input()))
m=(vet[0]*5 + vet[1]*2.5 + vet[2]*2.5)/10
print(round(m,2))
if(m>5):
	print("APROVADO")
else :
	print("REPROVADO")