from numpy import*
v = array(eval(input("qual vetor: ")))
v1 = array(zeros(2, dtype = int))
cont = 0
cont1 = 0
for i in range(0, size(v)):
	a = min(v)
	b = max(v)
c = (0.85 * a) + (0.15 * b)
d = (0.4 * a) + (0.6 * b)
for j in range(0, size(v)):
	if(v[j] >= a and v[j] < c):
		cont = cont + 1
for k in range(0, size(v)):
	if(v[k] >= d and v[k] < b):
		cont1 = cont1 + 1
v1[0] = cont 
v1[1] = cont1 
print(v1)