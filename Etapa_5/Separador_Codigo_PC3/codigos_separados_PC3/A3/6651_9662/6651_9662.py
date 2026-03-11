from numpy import*
v = array(eval(input("digite um vetor:")))
p = array([5, 4, 3, 2])
numerador = 0
denominador = 0
i = 0
while i<size(v):
	numerador = numerador + v[i]*p[i]
	denominador = sum(p)
	i = i+1
mp = numerador / denominador
print(round(mp, 2))