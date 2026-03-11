from numpy import*

alu = array(eval(input("")))
cont = 0

for i in range(size(alu)):
	if alu[i] >= 5:
		cont += 1
		
v = zeros(cont, dtype = int)
print(cont)
a = 0 
for i in range(size(alu)):
	if alu[i] >= 5:
		v[a] = i
		a = a + 1 
print(v)

		