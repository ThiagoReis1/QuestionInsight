from numpy import *
from numpy.linalg import *
t = array(eval(input("Qnt de turmas divisiveis: ")))

x = 0

for e in t:
	if e%5 == 0:
		x += 1
	
y = zeros(x,dtype = int)
x = 0

for i in range(len(t)):
	if t[i]%5 == 0:
		y[x] = i
		x +=1
		
print(x)
print(y)