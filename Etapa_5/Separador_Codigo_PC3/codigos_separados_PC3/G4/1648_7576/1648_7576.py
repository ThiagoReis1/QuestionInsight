from numpy import *

a = array(eval(input("insira: ")))
cont = 0

for i in range(len(a)):
	if a[i] < 70:
		cont += 1
k = 0
b = zeros(cont,dtype = int)
for j in range(len(a)):
	if(a[j] < 70):
		b[k] += j
		k += 1
		
print(cont)
print(b)