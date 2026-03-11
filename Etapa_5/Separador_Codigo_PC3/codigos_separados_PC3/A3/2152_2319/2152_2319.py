from numpy import*

v = array(eval(input(":")))

t = []
valor = 0	
for i in range(size((v))):
	if v[i] % 2 != 0:
		valor +=1
val = 0
vator2 = zeros(valor,dtype=int)

for j in range(size(v)):
	if v[j] % 2 != 0:
		vator2[val] = v[j]
		val += 1
print(vator2)
