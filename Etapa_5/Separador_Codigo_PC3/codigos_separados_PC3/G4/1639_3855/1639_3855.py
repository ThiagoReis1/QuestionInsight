from numpy import *

vet = array(eval(input()))

ac = 0
for i in range(size(vet)):
	if vet[i] % 2 ==0:
		ac= ac+1
	
print (ac)
v = zeros(ac, dtype=int)
j=0

for i in range(size(vet)):
	if vet [i] %2 ==0:
		v[j]=i
		j= j+1
		

print(v)
		
		