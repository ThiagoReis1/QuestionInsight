from numpy import *
s = input("digite: ").split(',')

vs = zeros(5, dtype=int)
for i in range(size(s)):
	if (s[i] == "CHN"):
		vs[0] = vs[0] + 1
	elif (s[i] == "JPN"):
		vs[1] = vs[1] + 1
	elif (s[i] == "KOR"):
		vs[2] = vs[2] + 1
	elif (s[i] == "MGL"):
		vs[3] = vs[3] + 1
	elif (s[i] == "THA"):
		vs[4] = vs[4] + 1
print(max(vs))
print(vs)
	