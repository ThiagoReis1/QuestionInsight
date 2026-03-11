from numpy import*

a = array(eval(input("")))

soma = 0

for i in range(size(a)):
	if a[i]%5== 0 :
		soma = soma + 1
print(soma)
vet = zeros(soma, dtype=int)
j = 0 
for i in range(size(a)):
	if a[i]%5==0:
		vet[j] = i 
		j = j + 1
print(vet)
	
	