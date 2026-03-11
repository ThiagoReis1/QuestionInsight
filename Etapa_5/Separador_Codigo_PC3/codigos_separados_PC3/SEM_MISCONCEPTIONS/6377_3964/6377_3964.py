string = input()
string = string.split(",")

vetor = [0, 0, 0, 0]

for i in string:
	if i == "A":
		vetor[0] += 1
	if i == "B":
		vetor[1] += 1
	if i == "C":
		vetor[2] += 1
	if i == "D":
		vetor[3] += 1
		
print(str(vetor).replace(",", ""))