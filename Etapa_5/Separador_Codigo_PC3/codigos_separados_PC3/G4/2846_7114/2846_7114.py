from numpy import * 

v = array(eval(input("vetor: ")))

g = zeros(size(v), dtype=int)

t = 0 

for i in range(size(v)):
	g[t] = 2*v[i]
	t = t + 1
	
print(g)