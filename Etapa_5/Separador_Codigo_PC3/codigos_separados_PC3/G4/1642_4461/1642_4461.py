from numpy import*

v = array(eval(input("vetor: ")))
c = 0
j = 0

for i in range(size(v)):
	if(v[i]%5 == 0):
		c = c +1
	
p = zeros(c,dtype=int)
for i in range(size(v)):
	if(v[i]%5 ==0):
		p[j] = i
		j = j + 1
print(c)
print(p)