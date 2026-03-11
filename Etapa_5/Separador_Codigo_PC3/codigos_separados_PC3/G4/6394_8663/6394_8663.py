from numpy import*
n = array(eval(input()))
ns = zeros(size(n), dtype=int)

for i in range(size(n)):
	if n[i] != 9:
		ns[i] += (n[i] + 1)

print(ns)
