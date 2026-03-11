from numpy import*
vi = array(eval(input(": ")))
cont = 0
cont1 = 0
i = 0

for i in range(size(vi)):
	if(vi[i] % 2 == 1):
		cont = cont + 1
n = zeros(cont, dtype=int)

for i in range(size(vi)):
	if(vi[i] % 2 == 1):
		n[cont1] = i
		cont1 = cont1 + 1
print(cont)
print(n)