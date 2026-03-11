from numpy import*
s = input("estado de origem: ").split(',')
vs = zeros(5, dtype=int)
p = 0
for i in range(size(s)):
	if (s[i] == "AC"):
		vs[0] = vs[0] + 1
	elif (s[i] == "AM"):
		vs[1] = vs[1] + 1
	elif (s[i] == "PA"):
		vs[2] = vs[2] + 1
	elif (s[i] == "RO"):
		vs[3] = vs[3] + 1
	elif (s[i] == "RR"):
		vs[4] = vs[4] + 1
p = p + 1
print(max(vs))
print(vs)

		