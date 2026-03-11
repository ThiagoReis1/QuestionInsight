from numpy import *
v = array(eval(input("vetor de notas: ")))

i = 1
s = 0
soma = 0
while(s < size(v)):
	soma = soma + v[s]*i
	i = i + 1
	s = s + 1
print(round(soma / 6, 2))