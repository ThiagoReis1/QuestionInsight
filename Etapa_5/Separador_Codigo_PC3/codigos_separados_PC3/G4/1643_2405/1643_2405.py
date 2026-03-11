from numpy import*
x = 0
vet = array(eval(input()))	

for i in vet:
	if(i >= 5):
		x = x + 1
print(x)

var = zeros(x , dtype = int)
j = 0

for i in range(size(vet)):
	if(vet[i] >= 5):
		var[j] = i
		j = j + 1
	
print(var)
		