from numpy import *
n = array(eval(input(":")))
v = 0
g = 0
i = 0
for x in n:
	if (x % 5) == 0:
		v += 1
		
print(v)
vet = zeros(v,dtype = int)
for i in range(size(n)) :
	if (n[i]% 5) == 0:
		vet[g] = i
		g +=1
print(vet)
