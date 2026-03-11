from numpy import*
vet = array(eval(input()))
i = 0
for x in vet:
	if(x<=50):
		i = i + 1
print(i)
nv = zeros(i, dtype=int)
j = 0
for x in range(size(vet)):
	if(vet[x]<=50):
		nv[j] = x
		j = j + 1
print(nv)