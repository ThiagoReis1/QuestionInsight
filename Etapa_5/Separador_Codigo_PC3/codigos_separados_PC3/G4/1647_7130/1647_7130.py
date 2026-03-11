from numpy import*

ap = array(eval(input("Quantidade de alunos aprovados: ")))
a = 0

for i in range(size(ap)):
	if ap[i] >= 70:
		a = a + 1
print(a)

c = zeros(a, dtype = int)
cont = 0

for j in range(size(ap)):
	if ap[j] >= 70:
		c[cont] = j
		cont = cont + 1
print(c)