from numpy import*
v = array(eval(input("Precos: ")))
i = 0
while(i<len(v)):
	if(v[i]>80):
		d = v[i] * 0.15
		v[i] = v[i] - d
		i = i + 1
	else:
		i = i + 1
i = 0
soma = 0
while(i<len(v)):
	soma = soma + v[i]
	i = i + 1
print(round(soma,2))
	