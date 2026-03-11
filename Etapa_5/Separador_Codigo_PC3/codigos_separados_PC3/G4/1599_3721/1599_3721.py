from numpy import*
v= array(eval(input("vetor")))
i=0
soma = sum(v)
while i <len(v):
	if v[i] > 80:
		v[i]= (v[i]/100)*85
	i+= 1
print(round(soma,2))