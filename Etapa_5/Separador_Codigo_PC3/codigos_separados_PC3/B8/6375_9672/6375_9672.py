from numpy import* 

votos= input("Insira A para votar no candidato A, B para o candidato B, C para o candidato C e D para o candidato D: ").upper().split(",")

zeros= zeros(4, dtype=int)

for i in range(size(votos)):
	if votos[i] == "A":
		zeros[0]= zeros[0] + 1
	elif votos[i] == "B":
		zeros[1]= zeros[1] + 1 
	elif votos[i] == "C":
		zeros[2]= zeros[2] + 1
	elif votos[i] == "D":
		zeros[3]= zeros[3] + 1
		
print(zeros)
		