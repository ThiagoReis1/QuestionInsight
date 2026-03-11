from numpy import*

entrada = array(eval(input("Digite entrada: ")))

# variavel acumuladora alunos aprovados
a = 0

for x in range(size(entrada)):
	if(entrada[x] >= 70):
		a = a + 1
z = 0
cont = zeros(a, dtype=int)
for y in range(size(entrada)):
	if (entrada[y] >= 70):
		cont[z] = y
		z = z + 1

print (a)
print(z)