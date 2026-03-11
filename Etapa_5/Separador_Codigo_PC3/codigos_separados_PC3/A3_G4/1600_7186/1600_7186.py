from numpy import*

l = array(eval(input()))
n = zeros(shape(l)[0], dtype = float)
m = 0
#v = l - l%0.15
#t = sum(v)

for i in range(shape(l)[0]):
	for j in range(shape(n)[0]):
		if(l[j] >= 80):
			m = m + 1
			v = l - (l % 0.15)
			t= sum(v)
		if(l[i]<=80):
			tv = sum(l)
			vt = t + tv
			m = m + 1
	print(round(tv,2))