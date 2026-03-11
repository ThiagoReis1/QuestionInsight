from numpy import*
v = array(eval(input("v: ")))
a = 0

for i in v:
	if(i >= 2000):
		
		a = a + 1
x = zeros(a,dtype=int)
j = 0
for i in range(size(v)):
	if(v[i] >= 2000):
		x[j] = i
		j = j + 1
		
		
		
print(a)
print(x)