from numpy import*
minimo = 0
v = array(eval(input("Informe o vetor: ")))
i = 0
l = 0
while(i < size(v)):
	if(minimo <= v[i]):
		l = l + 1
	i = i + 1
v1 = ones(l, dtype=float)
i = 0
i1 = 0
while(i < size(v)):
	if(minimo <= v[i]):
		v1[i1] = v[i]
		i1 = i1 + 1
	i = i + 1
print(v1)