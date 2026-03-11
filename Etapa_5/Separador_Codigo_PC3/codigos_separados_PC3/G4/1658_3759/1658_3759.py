from numpy import*
v = (input("Vetor:")).split(',')
c = 0
m = 0
k = 0
j = 0
t = 0
q = zeros(5, dtype=int)
for i in range(size(v)):
	if(v[i]== 'CHN'):
		c = c + 1
		q[0] = c
	elif(v[i]== 'JPN'):
		j = j + 1
		q[1] = j
	elif(v[i]== 'KOR'):
		k = k + 1
		q[2] = k
	elif(v[i]== 'MGL'):
		m = m + 1
		q[3] = m
	else:
		t = t +1
		q[4] = t
p = max(c,j,k,m,t)
print(p)
print(q)
 
