from numpy import *

num = array(eval(input("Numeros: ")))

i = 0

#vet = zeros(num,  dtype = int)

for i in range(size(num)):
	if(num[i] < 10):
		num[i] = num[i]*2
	i += 1
print(num)
	