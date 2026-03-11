from numpy import*
v = array(eval(input( )))
cont = zeros(v, dtype=int)
for i in range(size(v)):
	if(v[i]==1):
		cont[-1] = v[i]
	else:
		cont[0] = v[i]
print(cont)
