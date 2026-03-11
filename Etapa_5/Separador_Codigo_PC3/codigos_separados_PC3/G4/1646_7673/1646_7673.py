from numpy import * 

vet = array(eval(input()))

a = 0

for i in range(size(vet)):
	if(vet[i] <= 50):
		a = a + 1
print(a)

x = zeros(a, dtype = int)
y = 0

for i in range(size(vet)):
	if(vet[i] <= 50):
		x[y] = i
		y = y + 1
print(x)
	
	 
	

