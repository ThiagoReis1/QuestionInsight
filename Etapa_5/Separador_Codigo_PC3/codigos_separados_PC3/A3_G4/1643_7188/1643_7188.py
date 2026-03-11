from numpy import*
vet= array(eval(input()))
nap=0
ac=0
for i in range(size(vet)):
	if vet[i]>= 5:
		nap= nap +1
print(nap)
	
n= zeros(nap, dtype=int)
k=0
for j in range(size(vet)):
	if vet[j]>= 5:
		n[k]= j
		k= k+1
print(n)