from numpy import*

am = array(eval(input("matriculados: ")))
va = 0
c = 0

for i in range(size(am)):
	if (am[i] % 3==0):
		va = va + 1
print(va)

g=zeros(va, dtype = int)
for i in range(size(am)):
	if(am[c]%3==0 and ):
		g[c] = c
		c = c+1
	print(g)