from numpy import*
v = array(eval(input("")))
i = 0
qtd =0
j = 0
for i in range(size(v)):
	if(v[i] % 2 != 0):
		qtd += 1
z = zeros(qtd, dtype = int)
for i in range(size(v)):
	if(v[i] % 2 != 0):
		z[j] = i
		j += 1
print(qtd)
print(z)

	