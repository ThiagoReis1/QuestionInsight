from numpy import*
n = int(input("distancia de saltos:"))
vet = array(zeros(n,dtype=float))
c1 = 0
ind = 0
while(c1 < n):
	c2 = 0
	while(c2 < 5):
		vet[ind] = float(input("salto"))
		ind = ind + 1
		c2 = c2 + 1
	c1 = c1 + 1
c1 = ind = 0
while(c1 < n):
	c2 = 0
	soma = 0.0
	while(c2 < 5):
		soma = soma + vet[ind]
		ind = ind + 1
		c2 = c2 + 1
	c1 = c1 + 1
	print(round(soma/5,2))