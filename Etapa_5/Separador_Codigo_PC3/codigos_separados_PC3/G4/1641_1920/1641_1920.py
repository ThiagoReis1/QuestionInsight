from numpy import*
v = array(eval(input("Vetor:")))
ok = 0
for i in range(size(v)):
	if ((v[i]%3)==0):
		ok += 1
aux = zeros(ok,dtype=int)
print(ok)
for x in range(size(v)):
	u = 0
	if ((v[x]%3)==0):
		aux[u] = x
		u+=1
print(ok)
print(aux)