from numpy import*

cor = input("").upper().split(",")

cont = zeros(5, dtype=int)

for i in range(len(cor)):
	if cor[i] == "P":
		cont[0] += 1
	if cor[i] == "C":
		cont[1] += 1
	if cor[i] == "M":
		cont[2] += 1
	if cor[i] == "V":
		cont[3] += 1
	if cor[i] == "A":
		cont[4] += 1

print(max(cont))
print(cont)


