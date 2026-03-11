from numpy import*

v = array(eval(input()))
i = 0
custo = 0

while i < size(v):
	if v[i] > 200:
		v[i] = v[i]-v[i]*0.15
	i = i + 1
custo = sum(v)
print(round(custo,2))