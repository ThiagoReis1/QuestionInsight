from numpy import*
v = array(eval(input("")))
a = min(v)
b = max(v)
c = (0.6 * a) + (0.4 * b)
d = (0.3 * a) + (0.7 * b)
x = array(zeros(2, dtype = int))
q = 0
p = 0

for i in range(size(v)):
	if ((v[i] >= a) and (v[i] < c)):
		q = q + 1
		x[0] = q
	elif((v[i] >= c) and (v[i] < d)):
		p = p + 1
x[1] = p
print(x)



      


      


      