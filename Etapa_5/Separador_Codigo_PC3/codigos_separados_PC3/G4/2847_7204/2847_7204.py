from numpy import * 

v = array(eval(input("vetor: ")))

g = zeros(size(v), dtype=int)

t = 0  

for i in range(size(v)):
	g[t] = v[i]**2
	t = t + 1
	
print(g)