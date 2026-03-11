from numpy import*
vic=0

nvet= zeros(10,dtype= int)

for i in range(10):
	nvet[i] = float(input())
minn= int(input())
for i in range (10):
	if nvet[i] >= minn:
		vic= vic + 1
vet= zeros(vic,dtype= float)
j=0
for i in range(size(nvet)):
	if nvet[i] >= minn:
		vet[j] = nvet[i]
		j= j+1
print(vic)
print(vet)
