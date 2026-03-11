#Universidade Federal do Amazonas
#Icomp
#Larissa Magno Leao-21551610
#Exercicio 2

from numpy import*

p= float(input("Informe p:"))
x= array(eval(input("Informe o vetor x:")))
y= array(eval(input("Informe o vetor y:")))

t= p/(p-1)

cont=array(zeros(size(x),dtype=float))

for i in range(size(x)):
	cont[i]=x[i]-y[i]

soma= 0
for i in range(size(x)):
	soma= soma+abs(cont[i])**t

norma=soma**(1/t)
print(round(norma,6))