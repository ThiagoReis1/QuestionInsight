from numpy import *
s = input("Pais de origem: ").split(",")
vs = zeros(5, dtype = int)

for i in s:
	if (i == "BE"):
		vs[0] = vs[0] + 1
	elif (i == "ES"):
		vs[1] = vs[1] + 1
	elif (i == "FR"):
		vs[2] = vs[2] + 1
	elif (i == "IT"):
		vs[3] = vs[3] + 1
	elif (i == "PT"):
		vs[4] = vs[4] + 1

print(max(vs))
print(vs)
