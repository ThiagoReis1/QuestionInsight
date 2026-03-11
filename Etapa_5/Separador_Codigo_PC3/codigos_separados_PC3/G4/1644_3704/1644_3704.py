from numpy import*

v = array(eval(input('vet: ')))
p = 0
r = 0

for i in range(size(v)):
	if v[i]>= 5:
		p = p + 1
print(p)
#quntos reprovados
for j in range(size(v)):
	if v[j] < 5:
		r = r + 1

a = zeros(r, dtype=int)
x = 0
y = 0
for k in range(size(v)):

	if v[k] < 5:
		a[x] = v[y]
		x = x + 1
		y = y + 1
print(a)






		
	