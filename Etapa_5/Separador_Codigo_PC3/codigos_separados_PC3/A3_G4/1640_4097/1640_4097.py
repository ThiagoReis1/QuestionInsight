from numpy import*
v = array(eval(input("v: ")))

t = 0

for i in range(size(v)):
	if(v[i] % 2 != 0):
		t = t + 1
		
vi = zeros(v, dtype = int)
for o in range(size(v)):
	if(v[o] % 2 != 0):
		vi = v[o]
print(t)
print(vi)