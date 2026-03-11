from numpy import * 
nota = input("notas:").upper().split(",")
saida = zeros(4,dtype = int)
for i in range (len(nota)):
	if nota[i] == "C":
		saida[0] = saida[0] + 1
	elif nota[i] == "D":
		saida[1] = saida[1] + 1
	elif nota[i] == "V":
		saida[2] = saida[2] + 1
	elif nota[i] == "U":
		saida[3] = saida[3] + 1
print(saida)