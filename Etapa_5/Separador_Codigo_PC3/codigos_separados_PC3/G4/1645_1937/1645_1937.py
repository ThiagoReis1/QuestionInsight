from numpy import*

saque = array(eval(input()))

a = 0
q = 0

for i in range(size(saque)):
	if(saque[i] >= 2000):
		q = q + 1
	
v = zeros(q,dtype = int)

for i in range(size(saque)):
	if(saque[i] >= 2000):
		v[a] = i
		a = a + 1

print(q)
print(v)
