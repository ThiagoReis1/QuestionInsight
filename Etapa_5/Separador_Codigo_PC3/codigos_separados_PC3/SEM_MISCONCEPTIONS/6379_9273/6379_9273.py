from numpy import*

notas = input(" :").split(",")
count = zeros(5, dtype=int)

for i in range(size(notas)):
	if notas[i] == "A":
		count[0] = count[0] + 1
		
	if notas[i] == "B":
		count[1] = count[1] + 1
		
	if notas[i] == "C":
		count[2] = count[2] + 1
		
	if notas[i] == "D":
		count[3] = count[3] + 1
		
	if notas[i] == "E":
		count[4] = count[4] + 1
print(count)