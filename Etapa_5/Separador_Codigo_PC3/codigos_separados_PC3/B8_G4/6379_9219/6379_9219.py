from numpy import*
nota = input("(A/B/C/D/E)").split(",")
nv = zeros(5,dtype=int)

for i in nota:
	if i == "A":
		nv[0] = nv[0] + 1
		
	elif i == "B":
		nv[1] = nv[1] + 1
		
	elif i == "C":
		nv[2] = nv[2] + 1
		
	elif i == "D":
		nv[3] = nv[3] + 1
		
	elif i == "E":
		nv[4] = nv[4] + 1

print(nv)