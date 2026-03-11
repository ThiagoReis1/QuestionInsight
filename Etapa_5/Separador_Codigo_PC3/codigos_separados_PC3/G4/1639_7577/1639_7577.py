from numpy import*

vet = array(eval(input(": ")))
x = 0

for i in range(size(vet)):
	if vet[i] % 2 == 0:
		x = x + 1
var = zeros(x,dtype = int)
j = 0
for i in range(size(vet)):
	if vet [i] % 2 == 0:
		var[j] = i
		j=j+1
		
print(x)
print(var)
