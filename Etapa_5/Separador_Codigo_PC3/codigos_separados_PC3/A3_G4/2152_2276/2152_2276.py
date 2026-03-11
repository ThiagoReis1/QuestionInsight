from numpy import *
m = array(eval(input()))
p = 0
i = 0
g1 = zeros(p, dtype= int)
g2 = zeros(i, dtype= int)
for k in m:
	if k%2 == 0:
		p = p + 1	
	else: 
		i = i + 1
g2 = zeros(i, dtype= int)
x = 0
y = 0
while x < size(m):
	if m[x]%2 != 0:
		g2[y] = m[x] 
		y = y + 1
		x = x + 1
	else:
		x = x + 1
		
print(g2)
		