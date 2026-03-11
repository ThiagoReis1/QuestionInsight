from numpy import*

v = array(eval(input('vetor de precos: ')))
i = 0
while i < size(v) :
	if v[i] > 80 :
		v[i] = v[i] - 5
	else:
		v[i] = v[i]
	i = i + 1
print(round(sum(v),2))