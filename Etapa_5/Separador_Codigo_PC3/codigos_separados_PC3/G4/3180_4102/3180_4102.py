from numpy import*
s = array(eval(input("Sorotipos detectados: ")))
v = zeros(4, dtype=int)

for i in range(size(s)):
	if (s[i] == 1):
		v[0] = v[0]+1
	if (s[i] == 2):
		v[1] = v[1]+1
	if (s[i] == 3):
		v[2] = v[2]+1
	if (s[i] == 4):
		v[3] = v[3]+1
print(v)