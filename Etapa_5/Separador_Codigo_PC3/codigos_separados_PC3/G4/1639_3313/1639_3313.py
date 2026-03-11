from numpy import*
v = array(eval(input('numero de alunos: ')))
npar = 0
for i in range(size(v)):
	if(v[i]%2 == 0):
		npar = npar +1
print(npar)
cont = zeros(npar,dtype=int)
d = 0
for i in range(size(v)):
	if(v[i]%2 == 0):
		cont[d] = i
		d = d+1
				
print(cont)