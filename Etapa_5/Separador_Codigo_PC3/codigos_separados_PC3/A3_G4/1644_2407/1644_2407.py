from numpy import *
notas = array(eval(input("Notas: ")))

r = 0
a = 0
for n in (notas):
	if (n < 5):
		r = r + 1
		
v = zeros(r, dtype=int)
s = 0
for d in range(0, size(notas)):
	if (notas[d] < 5):
		v[s] = d
		s = s + 1

print(r)
print(v)