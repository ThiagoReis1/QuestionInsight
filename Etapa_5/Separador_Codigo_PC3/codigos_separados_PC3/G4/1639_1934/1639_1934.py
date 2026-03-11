from numpy import *

t = array(eval(input("Turmas: ")))

a = 0

for i in range(size(t)):
	if(t[i] % 2 == 0):
		a = a + 1
v = zeros(a, dtype = int)

i = 0

for j in range(size(t)):
	if(t[j] % 2 == 0):
		v[i] = j
		i = i + 1
	
print(a)
print(v)