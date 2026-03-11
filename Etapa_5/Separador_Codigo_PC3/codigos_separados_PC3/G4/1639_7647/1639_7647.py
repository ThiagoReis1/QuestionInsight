from numpy import*

a = array(eval(input("Insira a Quantidade de Alunos: ")))

vpar = 0

for i in range(size(a)):
	if(a[i] % 2 == 0):
		vpar = vpar + 1
		
v = zeros(vpar, dtype=int)
j = 0

for i in range(size(a)):
	if(a[i] % 2 == 0):
		v[j] = i
		j = j + 1
		
		
print(vpar)
print(v)
