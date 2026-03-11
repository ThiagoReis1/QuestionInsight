from numpy import*
cpf=array(eval(input("De o cpf: ")))
vetor=array([9,8,7,6,5,4,3,2,1])
i=0
total=0
while(i<9):
	total=total +cpf[i]*vetor[i]
	i=i+1
total=total%11
print(total)