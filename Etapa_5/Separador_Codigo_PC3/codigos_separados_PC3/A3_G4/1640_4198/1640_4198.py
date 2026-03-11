from numpy import*
a= array(eval(input("Digite o vetor quantidade de alunos: ")))
impar= 0
for i in range(size(a)):
	if(a[i]%2!=0):
		impar= impar + 1
print(impar)
cont= 0
b= 0
for i in range(size(a)):
	if(a[i]%2!=0):
		[cont]= i
		cont= cont + 1
print()
		


	