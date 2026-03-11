from numpy import*
v = array(eval(input()))
i = 0
for a in range(size(v)):
	if(v[a] >= 70):
		i = i + 1
print(i) # n.de alunos aprov.
d = zeros(i, dtype = int)
j = 0
for b in range(size(v)):
	if(v[b] >= 70):
		d[j] = b
		j = j + 1
print(d)		