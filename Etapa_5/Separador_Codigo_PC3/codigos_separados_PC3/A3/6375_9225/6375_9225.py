from numpy import*

votos = input(":").split(",")
count = zeros(4,dtype=int)
i = 0

total = 0

for i in range(size(votos)):
	if votos[i] == "A":
		count[0] = count[0] + 1
	if votos[i] == "B":
		count[1] = count[1] + 1
	if votos[i] == "C":
		count[2] = count[2] + 1
	if votos[i] == "D":
		count[3] = count[3] + 1
		
print(count)
kk