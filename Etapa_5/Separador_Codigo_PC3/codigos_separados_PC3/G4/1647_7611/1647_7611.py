from numpy import*

a = array(eval(input('Escreva a porcentagem de presenca dos alunos: ')))
ap = 0
g = 0
for i in range(size(a)):
	if a[i] >= 70:
		ap += 1

#print(ap)
v = zeros(ap, dtype = int)
#print(v)

for i in range(size(a)):
	if a[i] >= 70:
		v[g] = i
		g+=1
	
print(ap)
print(v)