from numpy import*
v = array(eval(input(": ")))

soma = 0

for i in range(size(v)):
	if(v[i]>80):
		v[i] -= 5
	soma =round( (soma + v[i]), 2)
print(soma)