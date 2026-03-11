from numpy import*
# limites validos
minimo = 0
# vetor
v = array(eval(input("Digite o vetor: ")))
i = 0
l = 0
while(i < size(v)):
	if(minimo <= v[i]):
		l = l + 1
	i = i + 1
# formacao do vetor resultante
v1 = ones(l, dtype=float)
i = 0
i1 = 0
while(i < size(v)):
	if(minimo <= v[i]):
		v1[i1] = v[i]
		i1 = i1 + 1
	i = i + 1
print(v1)