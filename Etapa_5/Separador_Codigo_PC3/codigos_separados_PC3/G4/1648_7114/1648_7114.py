from numpy import * 

v = array(eval(input("vetor da presenca: ")))

p = 0

for i in range(size(v)):
	if v[i] < 70:
		p = p + 1
		
g = zeros(p, dtype=int)

t = 0
for i in range(size(v)):
	if v[i] < 70:
		g[t] = i
		t = t + 1
		
print(p)
print(g)

