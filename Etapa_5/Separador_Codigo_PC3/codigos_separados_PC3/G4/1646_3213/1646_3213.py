from numpy import * 

sa = array(eval(input("Saques: ")))

l = 0
for j in sa:
	if (j <= 50):
		l = l + 1
		
vs = zeros(l, dtype=int)
i = 0
for f in range(size(sa)):
	if (sa[f] <= 50):
		vs[i] = vs[i] + f
		i = i + 1
print(l)
print(vs)