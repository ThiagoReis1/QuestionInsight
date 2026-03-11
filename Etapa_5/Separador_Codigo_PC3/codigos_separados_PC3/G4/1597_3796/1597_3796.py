from numpy import*
v = array(eval(input("vetor")))
i = 0
while i < len(v):
	if v[i] > 80:
		v[i] = (v[i]/100)*85
	i += 1
soma = sum(v)
print(round(soma,2))