from numpy import *
a = eval(input())
x = 0
y = 0
vet = zeros(size(a))
while(x < size(a)):
	if(a[x]>-100):
		vet[y] = a[x]
		y = y + 1
	x = x + 1
vet2 = zeros(y)
z = 0
y = 0
while(z < size(vet)):
	if(vet[z]!=0):
		vet2[y] = vet[z]
		y = y + 1
	z = z + 1
print(vet2)
