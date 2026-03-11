from numpy import*


cont=0
soma=0.0
while cont <5:
	n=float(input())
	soma=soma+n
	cont=cont+1

	m=soma/5

if m > 5 :
	print(round(m,1))
	print("Aprovado")
	
else:
	print(round(m,1))
	print("Reprovado")
	