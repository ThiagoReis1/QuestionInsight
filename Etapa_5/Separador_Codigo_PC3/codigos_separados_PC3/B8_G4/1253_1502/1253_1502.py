from numpy import*
v = array(eval(input("insira o primeiro vetor: ")))  
a = min(v)
b = max(v)
c = (0.6 * a) + (0.4 * b)
d = (0.3 * a) + (0.7 * b)

m = array(zeros(2, dtype = int))
q = 0
p = 0
for x in range(size(v)):
	if((v[x] >= a) and (v[x] < c)):
		q = q + 1
		m[0] = q
	elif((v[x] >= d) and (v[x] < b)):
		p = p + 1
m[1] = p
print(m)

