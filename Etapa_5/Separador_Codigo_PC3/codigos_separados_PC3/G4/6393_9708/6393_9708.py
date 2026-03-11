from numpy import*
v = array(eval(input()))
cont = zeros(size(v),dtype=int)
for i in range(size(v)):
	if v[i] == 9:
		cont[i] = 0
	else:
		cont[i] = v[i]+1
print(cont**3)