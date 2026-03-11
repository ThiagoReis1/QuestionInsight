from numpy import*

qam = array(eval(input()))

c = 0
f = 0
g = 0

for i in range(size(qam)):
	if(qam[i]%2 != 0):
		c = c + 1
print(c)
z = zeros(c, dtype=int)

for j in range(size(z)):
	f = 0
	g = 0
	if(qam[j]%2 != 0):
		j = j 
z[0] = z[0] + j[j]
z[1] = z[1] + j[j]
z[2] = z[2] + j[j]

print(z)
	