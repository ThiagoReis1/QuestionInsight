from numpy import*

t = array(eval(input( )))
n = 0
j = 0

for i in range(size(t)):
	if(t[i] % 5 == 0):
		n = n+1
p = zeros(n, dtype = int)
for i in range(size(t)):
	if (t[i]%5 == 0):
		p[j] = i
		j = j+1
print(n)
print(p)