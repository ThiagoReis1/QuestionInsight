vetor = [0,0,0,0]
gols = input().split(",")
for i in range (len(gols)):
	if gols[i].upper() == "A":
		vetor[0] +=1
	elif gols[i].upper() == "B":
		vetor[1] += 1
	elif gols[i].upper() == "C":
		vetor[2] += 1
	elif gols[i].upper() == "D":
		vetor[3] +=1
		
print("[{} {} {} {}]".format(vetor[0],vetor[1],vetor[2],vetor[3]))