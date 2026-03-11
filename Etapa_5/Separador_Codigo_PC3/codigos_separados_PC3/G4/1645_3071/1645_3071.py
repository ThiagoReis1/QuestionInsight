from numpy import*
vs = array(eval(input("vetor saque: ")))

#acumuladora de saques acima do limite
sa = 0 

for i in range(size(vs)):
	if (vs[i] >= 2000):
		sa = sa + 1
	
nv = zeros(sa, dtype=int)
#indice da posicao do vetor de saida
ps = 0

for i in range(size(vs)):
	if (vs[i] >= 2000):
		nv[ps] = i
		ps = ps + 1
print(sa)
print(nv)