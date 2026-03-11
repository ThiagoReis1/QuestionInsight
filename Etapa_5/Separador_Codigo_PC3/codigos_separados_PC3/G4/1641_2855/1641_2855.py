from numpy import* 

v = array(eval(input("turmas:")))
i = 0

for n in v:
	if(n%3==0):
		i = i + 1
		
vtor = zeros(i, dtype =int)
p = 0
p2 = 0
for nc in v:
	if(nc%3==0):
		vtor[p] = p2
		p = p + 1
	p2 = p2 + 1
print(i)
print(vtor)