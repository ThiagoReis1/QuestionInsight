from numpy import*

n = input()
vetor = n.split(',')

estados = zeros(5, dtype=int)

for i in vetor:
	if i == "AM":
		estados[0]=estados[0]+1
	elif i == "PE":
		estados[1]=estados[1]+1
	elif i == "MG":
		estados[2]=estados[2]+1
	elif i == "SP":
		estados[3]=estados[3]+1
	elif i == "RS":
		estados[4]=estados[4]+1

print(max(estados))
print(estados)
	