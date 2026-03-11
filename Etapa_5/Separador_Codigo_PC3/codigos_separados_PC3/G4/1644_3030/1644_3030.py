from numpy import*
from math import*
n = array(eval(input("Quais as notas?")))
rep = 0
for i in range(size(n)):
	if(n[i] < 5.0):
		rep = rep + 1
print(rep)
z = zeros(rep, dtype=int)
x = 0
i = 0
while(i < size(n)):
	if(n[i] < 5.0):
		z[x] = i
		x = x + 1
		i = i + 1
	else:
		i = i +1
print(z)