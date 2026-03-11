from numpy import*

v = array(eval(input(" coloque o vetor: ")))
a = 0

for i in range(size(v)):
	if v[i] > 80:
		b = v[i] - (v[i] * (15/100))
		a = b + a
	else:
		a = a + v[i]
		
print(round(a , 2))