from numpy import*
ent = input("").split(",")
nent = zeros(4, dtype = int)
for i in range(size(ent)):
	if(ent[i] == "O"):
		nent[0] = nent[0] + 1
	if(ent[i] == "D"):
		nent[1] = nent[1] + 1
	if(ent[i] == "N"):
		nent[2] = nent[2] + 1
	if(ent[i] == "C"):
		nent[3] = nent[3] + 1
print(nent)