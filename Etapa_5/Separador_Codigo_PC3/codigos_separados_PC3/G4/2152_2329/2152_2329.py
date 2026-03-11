from numpy import*
f = array(eval(input(":")))
npar = 0
for  x in f:
	if (x % 2 != 0 ):
		npar = npar + 1
cont=zeros(npar, dtype=int)
i = 0

for t in f:
	
	if (t % 2 != 0 ):
		cont[i]= cont[i] + t
		i =i + 1
print(cont)