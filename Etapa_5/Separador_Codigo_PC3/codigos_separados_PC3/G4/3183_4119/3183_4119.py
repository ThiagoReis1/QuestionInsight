from numpy import*
v = array(eval(input("vetor: ")))
v2 = zeros(size(v), dtype=int)
for i in size(v):
	v2[i] = v[-1]
print(2)