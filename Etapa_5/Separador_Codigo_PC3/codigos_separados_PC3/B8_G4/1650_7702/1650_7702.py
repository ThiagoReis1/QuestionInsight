from numpy import*
c =input("cabelo: ").upper().split(',')
cont = zeros(5, dtype=int)

for i in range(len(c)):
	if c[i] == "P":
		cont[0] += 1
	elif c[i] == "C":
		cont[1] += 1
	elif c[i] == "R":
		cont[2] += 1
	elif c[i] == "L":
		cont[3] +=1
	elif c[i] == "B":
		cont[4] += 1
print(max(cont))
print(cont)
