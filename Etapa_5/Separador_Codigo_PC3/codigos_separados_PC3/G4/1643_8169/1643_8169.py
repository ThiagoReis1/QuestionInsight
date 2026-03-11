from numpy import*
v = array(eval(input("Notas: ")))
q = 0
for i in range(size(v)):
	if v[i] >= 5.0:
		q = q + 1
print(q)
s = zeros(q,dtype=int)
c = 0
for x in range(size(v)): 
	if v[x] >= 5.0:
		s[c]=x
		c += 1 
print(s)
		