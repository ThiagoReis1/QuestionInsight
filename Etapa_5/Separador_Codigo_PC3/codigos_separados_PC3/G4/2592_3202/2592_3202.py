from numpy import * 
v = array(eval(input()))
ar = 0 
pv = 0
pf = 0
for x in v:
	if( x >= 60):
		ar= ar + 1
print(ar)
f = zeros(ar, dtype=int)
for i in v:
	if(i >= v[0]):
		f[pf] = pv
		pf = pf + 1
	pv = pv + 1
i = i + 1

for p in f:
	print(p)