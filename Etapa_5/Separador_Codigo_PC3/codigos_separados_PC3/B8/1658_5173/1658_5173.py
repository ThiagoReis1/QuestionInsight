from numpy import * 

vetor = array(input("entre com: ").split(","))

acumu = zeros(5,dtype=int)
		
for i in range(size(vetor)):
	if vetor[i] == "CHN":
		acumu[0] += 1
	elif vetor[i] == "JPN":
		acumu[1] += 1 
	elif vetor[i] == "KOR":
		acumu[2] += 1
	elif vetor[i] == "MGL":
		acumu[3] += 1
	elif vetor[i] == "THA":
		acumu[4] += 1
		
maior = 0

for i in range(size(acumu)):
	if acumu[i] > maior:
		maior = acumu[i]
print((maior))
print(acumu)