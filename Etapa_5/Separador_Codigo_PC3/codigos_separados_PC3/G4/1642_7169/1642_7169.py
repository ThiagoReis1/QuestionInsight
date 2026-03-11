from numpy import*
vet = array(eval(input("quantas turmas ")))
i = 0
for x in range(size(vet)):
	if vet[x] > 5.0:
		i = i + 1 
zero = zeros(i,dtype=int)
print(i)
j = 0
for x in range(len(vet)):
	if vet[x] < 5.0:
		zero[j] = x
		j = j +1 
print(zero)