from numpy import *

v = array(eval(input("Vetor: ")))

t = zeros(4, dtype=int)
for i in range(size(v)):
	if v[i] == "BOTAFOGO":
		t[0] += 1
	elif v[i] == "FLAMENGO":
		t[1] += 1
	elif v[i] == "FLUMINENSE":
		t[2] += 1
	else:
		t[3] += 1
print(t)