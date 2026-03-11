from numpy import*

reprovados= array(eval(input("Digite o numero de alunos reprovados:")))
cont= 0
a=0
for i in range(size(reprovados)):
	if(reprovados[i] < 70):
		cont = cont + 1
print(cont)

a = zeros(cont, dtype = int)

cont1= 0

for i in range(size(reprovados)):
	if(reprovados[i] < 70):
		a(cont1) = i
		cont = cont + 1 
print(a)