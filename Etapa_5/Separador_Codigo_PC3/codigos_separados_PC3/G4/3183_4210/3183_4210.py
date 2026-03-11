from numpy import*
vet = array(eval(input("decrescente:")))
novo = zeros(size(vet),dtype=int)
j = - 1
for i in range(size(vet)):
	novo[i] = vet[j]
	j = j - 1
print(novo)