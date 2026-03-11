from numpy import*

ent = array(eval(input("vetor:")))

sa = 0

for i in ent:
	if i<=50:
		sa = sa + 1
print(sa)

aux = zeros(sa, dtype=int)
r = 0
for i in range(size(ent)):
	if ent[i] <= 50:
		aux[r] = i
		r+=1
print(aux)