from numpy import*
v = array(eval(input("vetor: ")))
a = 0
for i in v:
	if (i >= 70):
		a = a + 1
		
v2 = zeros(a, dtype = int)
r = 0
for n in range(size(v)):
	if(v[n] >=70):
		v2[r] = n
		r = r + 1
		
print(a)		
print(v2)
