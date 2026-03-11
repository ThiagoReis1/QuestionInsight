from numpy import*
saques = array(eval(input('Saques: ')))
vsup = 0

for i in saques:
	if i >= 2000.00:
		vsup+=1
print(vsup)

vet = zeros(vsup,dtype=int)
c = 0
for i in range(0,size(saques)):
	if saques[i] >= 2000.00:
		vet[c] = i
		c+=1
print(vet)