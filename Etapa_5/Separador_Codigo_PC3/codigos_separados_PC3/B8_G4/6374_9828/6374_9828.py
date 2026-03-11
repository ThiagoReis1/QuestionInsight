from numpy import *
co = input("C: ").split(",")
f = zeros(4,dtype=int)

for i in range(0,len(co)):
	if co[i] == "O" or co[i] == "o":
		f[0] += 1
	elif co[i] == "D" or co[i] == "d":
		f[1] += 1
	elif co[i] == "N" or co[i] == "n":
		f[2] += 1
	elif co[i] == "C" or co[i] == "c":
		f[3] += 1
print(f)