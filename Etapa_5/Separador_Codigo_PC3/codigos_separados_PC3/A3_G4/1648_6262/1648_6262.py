from numpy import*

nota = array(eval(input("Digite a frequencia: ")))
cont = 0
a = 0
for i in range(size(nota)):
	if(nota[i] < 70):
		cont = cont + 1
print(cont)

a = zeros(cont, dtype = int)

cont1 = 0

for i in range(size(nota)):
	if(nota[i] < 70):
		a[cont1] = i
		cont1 = cont1 + 1

print(a)