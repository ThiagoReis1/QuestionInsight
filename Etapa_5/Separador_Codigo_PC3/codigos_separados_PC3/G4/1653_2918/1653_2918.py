from numpy import*

na = input ("insira a nacionalidade: ")
na = na.split(',')

a = 0
b = 0
c = 0
co = 0
u = 0

z = zeros(5,dtype=int)

for i in range(size(na)):
	if na[i] == 'AR':
		a = a + 1
for i in range(size(na)):
	if na[i] == 'BR':
		b = b + 1
for i in range(size(na)):
	if na[i] == 'CL':
		c = c + 1
for i in range(size(na)):
	if na[i] == 'CO':
		co = co + 1
for i in range(size(na)):
	if na[i] == 'UY':
		u = u + 1
		
z[0] = a
z[1] = b
z[2] = c
z[3] = co
z[4] = u

print(max(z))
print(z)