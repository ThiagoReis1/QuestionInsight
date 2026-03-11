from numpy import*
v = array(eval(input("As temperaturas sao:")))

i = 0
l = size(v)
negativo = 0
while (i < size (v)):
	if(v[i] > 40):
		negativo = negativo + 1
	i = i + 1
l = size(v) - negativo
i = 0 
k = 0
v2 = array(ones(l, dtype = float))
while ( i < size(v)):
	if(v[i] <= 40):
		v2[k] = v[i]
		k = k + 1
	i = i + 1
print(v2)