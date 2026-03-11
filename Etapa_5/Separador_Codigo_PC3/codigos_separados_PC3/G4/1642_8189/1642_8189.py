from numpy import*
v= array(eval(input(": ")))
cont = 0
cont1 = 0
i = 0

for i in range(size(v)):
	if (v[i] %5 == 0):
		cont = cont + 1
z = zeros(cont,dtype=int)

for i in range(size(v)):
	if (v[i] %5 == 0):
		z [cont1] = i
		cont1 = cont1 + 1
print(cont)
print(z)