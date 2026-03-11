from numpy import *

v = array(eval(input("tempo de banho: ")))
vperc = array(eval(input("percentual de abertura: ")))

i = 0
soma = 0
v[0] = vperc[0]

# 0,05L por %

while(i < size(v)):
	v[i] = vperc[i]

	soma = soma + (v[i]) * (vperc[i]/100)
	i = i + 1

print(round(soma, 2))
	