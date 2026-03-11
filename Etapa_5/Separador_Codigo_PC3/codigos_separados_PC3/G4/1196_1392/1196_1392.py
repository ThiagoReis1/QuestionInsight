from numpy import*
#limites invalidos
minimo = -60
maximo = 60
#vetor
v = array(eval(input("Digite o vetor: ")))
i = 0
l = 0
while(i < size(v)):
	if((minimo < v[i]) and (v[i] < maximo)):
		l = l + 1
	i = i + 1
#formação do vetor resultante
v1 = ones(l, dtype=float)
i = 0
i1 = 0
while(i < size(v)):
	if((minimo < v[i]) and (v[i] < maximo)):
		v1[i1] = v[i]
		i1 = i1 + 1
	i = i + 1
print(v1)
	
