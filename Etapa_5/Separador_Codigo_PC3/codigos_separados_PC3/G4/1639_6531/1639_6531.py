from numpy import*
vet = array(eval(input('numeros de alunos: ')))

qt = 0

for i in range(size(vet)):
	if(vet[i] % 2 == 0):
		qt = qt + 1
z = zeros(qt, dtype=int)
cont = 0
for j in range(size(vet)):
	if(vet[j] % 2 == 0):
		z[cont] = z[cont] + j
		cont = cont + 1

		

print(qt)
print(z)
	

	

	



		
		