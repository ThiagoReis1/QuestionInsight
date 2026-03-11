from numpy import*
v = array(eval(input("Informe o vetor: ")))
n = size(v)
i=0
ii=0
j=0
jj=0
for a in v:
	if(a == 1):
		i = i + 1
	if(a == 2):
		ii = ii + 1
	if(a == 3):
		j = j + 1
	if(a == 4):
		jj = jj + 1
x = array([i,ii,j,jj])
print(x)