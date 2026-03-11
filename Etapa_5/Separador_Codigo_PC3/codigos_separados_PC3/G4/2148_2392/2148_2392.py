from numpy import*
vet = eval(input())
print(sum(vet))
i = 0
for x in range(size(vet)):
	if(vet[x]>=5):
		i = i + 1
print(i)