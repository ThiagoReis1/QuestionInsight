#Julia Pacheco
#25 de Agosto de 2016
#Av 06 Ex01

from numpy import*
#ler vetor
v = array(eval(input("v: ")))
#valores A e B
A = min(v)
B = max(v)
#valores de C e D
C = (0.7*A) + (0.3*B)
D = (0.4*A) + (0.6*B)
#variaveis de controle
i = 0
x = array(zeros(2, dtype=int))
#verificacao
for i in range(size(v)):
	if(v[i] >= C and v[i] < D):
		x[0] = x[0] + 1
	else:
		if(v[i] >= D and v[i] < B):
			x[1] = x[1] + 1
print(x)
